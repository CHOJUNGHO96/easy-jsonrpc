# Easy JSON-RPC

Python의 jsonrpclib-pelix(jsonrpclib의 Python 3 호환 포크)와 Go의 github.com/filecoin-project/go-jsonrpc 간의 호환성을 제공하는 JSON-RPC 라이브러리입니다. 이 라이브러리를 사용하면 Python과 Go 애플리케이션 간에 쉽게 JSON-RPC 통신을 구현할 수 있습니다.

## 특징

- Python 3.5 ~ 3.9 지원
- Python(jsonrpclib-pelix)과 Go(github.com/filecoin-project/go-jsonrpc) 간의 상호 운용성
- 간단한 API로 쉬운 사용
- 양방향 통신 및 알림(단방향) 지원
- 자동 메서드 등록 및 네임스페이스 관리
- Python과 Go 환경 간의 호환성 문제 자동 해결

## 시스템 요구 사항

- Python 3.5, 3.6, 3.7, 3.8, 3.9 (이 라이브러리는 현재 Python 3.10 이상에서는 테스트되지 않았습니다)
- Go 클라이언트 사용시: Go 1.13 이상 및 github.com/filecoin-project/go-jsonrpc 라이브러리

## 라이브러리 통합

이 라이브러리는 다음 두 가지 주요 JSON-RPC 라이브러리를 통합하여 사용합니다:
- **Python 측**: [jsonrpclib-pelix](https://pypi.org/project/jsonrpclib-pelix/) - 원래 jsonrpclib의 Python 3 호환 포크로, Python 기반 JSON-RPC 서버 및 클라이언트 구현 제공
- **Go 측**: [github.com/filecoin-project/go-jsonrpc](https://github.com/filecoin-project/go-jsonrpc) - Go 기반 JSON-RPC 클라이언트 및 서버 구현

## 중요 설정 옵션

### 서버 측 옵션

**`allow_go_client`**: Go 클라이언트가 이 서버에 연결할 수 있도록 하는 옵션

- **`allow_go_client=True`** (기본값): 
  - Go 클라이언트와의 호환성 기능을 활성화합니다.
  - 각 메서드가 등록될 때 Go 클라이언트를 위한 특별한 형식의 메서드 이름도 함께 등록됩니다.
  - Go 클라이언트가 이 서버에 연결해야 하는 경우 이 옵션을 활성화해야 합니다.

- **`allow_go_client=False`**:
  - Python 클라이언트만 사용하는 경우에 적합합니다.
  - 메서드 등록이 더 간단하고 효율적입니다.
  - Go 클라이언트는 이 서버에 연결할 수 없습니다.

사용 예시:
```python
# Go 클라이언트와 Python 클라이언트 모두 지원
server = EasyJSONRPCServer('localhost', 8080, allow_go_client=True)

# Python 클라이언트만 지원 (더 간단한 처리)
server = EasyJSONRPCServer('localhost', 8080, allow_go_client=False)
```

### 클라이언트 측 옵션

**`is_go_server`**: 클라이언트가 Go 서버에 연결하는지 여부를 지정하는 옵션

- **`is_go_server=True`**:
  - Go로 작성된 서버에 연결할 때 사용합니다.
  - 메서드 이름과 매개변수를 Go 서버가 이해할 수 있는 형식으로 변환합니다.
  - 응답 및 오류 처리도 Go 서버에 맞게 조정됩니다.

- **`is_go_server=False`** (기본값):
  - Python으로 작성된 서버에 연결할 때 사용합니다.
  - 표준 jsonrpclib 프로토콜을 사용하며, 특별한 변환이 적용되지 않습니다.

사용 예시:
```python
# Python 서버에 연결
client = EasyJSONRPCClient('http://localhost:8080', is_go_server=False)

# Go 서버에 연결
client = EasyJSONRPCClient('http://localhost:8080', is_go_server=True)
```

## ⚠️ 중요 주의사항: Go와 Python 간의 함수 명명 규칙

Go와 Python은 함수/메서드 이름 지정 규칙이 다릅니다:
- **Go**: UpperCamelCase 사용 (예: `Add`, `GetValue`, `CalculateTotal`)
- **Python**: 일반적으로 snake_case 사용 (예: `add`, `get_value`, `calculate_total`)

**Go 클라이언트와 통신할 경우**:
- Python에서 함수/메서드를 정의할 때는 **반드시 Go 스타일(UpperCamelCase)** 을 사용해야 합니다.
- 예를 들어, Go 클라이언트에서 `Calculator.Add` 메서드를 호출하려면 Python 서버에서도 `Calculator` 클래스의 메서드 이름을 `Add`로 정의해야 합니다 (`add`가 아님).

**클래스 메서드 호출 시 네임스페이스 지정**:
- Python 서버에서 클래스를 등록한 경우, Go 클라이언트에서는 클라이언트 생성 시 네임스페이스를 올바르게 지정해야 합니다.
- 독립적인 함수만 호출하는 경우: `jsonrpc.NewClient(context.Background(), "http://localhost:8080", "", &client, nil)`
- 클래스 메서드를 호출하는 경우: `jsonrpc.NewClient(context.Background(), "http://localhost:8080", "클래스명", &client, nil)`

잘못된 예:
```python
def add(params):  # snake_case - Go 클라이언트에서 호출 불가
    a = params.get("a", 0)
    b = params.get("b", 0)
    return a + b
```

올바른 예:
```python
def Add(params):  # UpperCamelCase - Go 클라이언트에서 호출 가능
    a = params.get("a", 0)
    b = params.get("b", 0)
    return a + b
```

이 명명 규칙 차이를 무시하면 Go 클라이언트에서 "Method not supported" 오류가 발생할 수 있습니다.

## 설치

```bash
pip install easy-jsonrpc
```

## 간단한 사용법

### 서버 예제

```python
from easy_jsonrpc import EasyJSONRPCServer

# 간단한 함수 정의 (Go 클라이언트 지원을 위해 UpperCamelCase 사용)
def Hello(params):
    name = params.get("name", "World")
    return f"Hello, {name}!"

def Add(params):
    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    return a + b

# 서버 초기화 및 실행
server = EasyJSONRPCServer('localhost', 8080, allow_go_client=True)
server.register_function(Hello)
server.register_function(Add)
server.start()
```

### Python 클라이언트 예제 (jsonrpclib-pelix 사용)

```python
from easy_jsonrpc import EasyJSONRPCClient

# 클라이언트 초기화
client = EasyJSONRPCClient('http://localhost:8080')

# hello 메서드 호출
result = client.call('Hello', {"name": "Alice"})
print(result)  # 출력: Hello, Alice!

# add 메서드 호출
sum_result = client.call('Add', {"a": 5, "b": 3})
print(sum_result)  # 출력: 8

# 알림 전송 (응답 기다리지 않음)
client.notify('Hello', {"name": "Notification"})
```

### Go 클라이언트 예제 (github.com/filecoin-project/go-jsonrpc 사용)

```go
package main

import (
    "context"
    "fmt"
    "github.com/filecoin-project/go-jsonrpc"
)

func main() {
    // 클라이언트 생성
    var client struct {
        Hello func(ctx context.Context, params map[string]interface{}) (string, error)
        Add   func(ctx context.Context, params map[string]interface{}) (int, error)
    }
    // 독립적인 함수 호출을 위해 네임스페이스는 빈 문자열("")로 지정
    closer, err := jsonrpc.NewClient(context.Background(), "http://localhost:8080", "", &client, nil)
    if err != nil {
        panic(err)
    }
    defer closer()

    // Hello 메서드 호출
    params := map[string]interface{}{
        "name": "Bob",
    }
    result, err := client.Hello(context.Background(), params)
    if err != nil {
        panic(err)
    }
    fmt.Println(result)  // 출력: Hello, Bob!

    // Add 메서드 호출
    addParams := map[string]interface{}{
        "a": 10,
        "b": 20,
    }
    sum, err := client.Add(context.Background(), addParams)
    if err != nil {
        panic(err)
    }
    fmt.Println("Sum:", sum)  // 출력: Sum: 30
}
```

## 클래스 등록 예제

### 서버 측: Calculator 클래스 등록

```python
from easy_jsonrpc import EasyJSONRPCServer

# 계산기 클래스 정의 (Go 호환을 위해 UpperCamelCase 메서드 이름 사용)
class Calculator:
    def Add(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a + b
        
    def Subtract(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a - b
        
    def Multiply(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a * b
        
    def Divide(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 1))  # 0으로 나누기 방지
        if b == 0:
            return "Error: Division by zero"
        return a / b

# 서버 초기화 및 클래스 등록
server = EasyJSONRPCServer('localhost', 8080, allow_go_client=True)
server.register_class(Calculator)  # Calculator의 모든 메서드 등록
server.start()
```

### Python 클라이언트: Calculator 사용

```python
from easy_jsonrpc import EasyJSONRPCClient

# 클라이언트 초기화
client = EasyJSONRPCClient('http://localhost:8080')

# Calculator 클래스의 메서드 호출
add_result = client.call('Calculator.Add', {"a": 10, "b": 5})
print(f"10 + 5 = {add_result}")  # 출력: 10 + 5 = 15

subtract_result = client.call('Calculator.Subtract', {"a": 10, "b": 5})
print(f"10 - 5 = {subtract_result}")  # 출력: 10 - 5 = 5

multiply_result = client.call('Calculator.Multiply', {"a": 10, "b": 5})
print(f"10 * 5 = {multiply_result}")  # 출력: 10 * 5 = 50

divide_result = client.call('Calculator.Divide', {"a": 10, "b": 5})
print(f"10 / 5 = {divide_result}")  # 출력: 10 / 5 = 2.0
```

### Go 클라이언트: Calculator 사용

```go
package main

import (
	"context"
	"fmt"
	"github.com/filecoin-project/go-jsonrpc"
)

func main() {
	// 클라이언트 생성
	var client struct {
		Add      func(ctx context.Context, params map[string]interface{}) (int, error)
		Subtract func(ctx context.Context, params map[string]interface{}) (int, error)
		Multiply func(ctx context.Context, params map[string]interface{}) (int, error)
		Divide   func(ctx context.Context, params map[string]interface{}) (float64, error)
	}

	closer, err := jsonrpc.NewClient(context.Background(), "http://localhost:8080", "Calculator", &client, nil)
	if err != nil {
		panic(err)
	}
	defer closer()

	// Calculator.Add 메서드 호출
	addParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	addResult, err := client.Add(context.Background(), addParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 + 5 = %d\n", addResult) // 출력: 10 + 5 = 15

	// Calculator.Subtract 메서드 호출
	subtractParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	subtractResult, err := client.Subtract(context.Background(), subtractParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 - 5 = %d\n", subtractResult) // 출력: 10 - 5 = 5

	// Calculator.Multiply 메서드 호출
	multiplyParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	multiplyResult, err := client.Multiply(context.Background(), multiplyParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 * 5 = %d\n", multiplyResult) // 출력: 10 * 5 = 50

	// Calculator.Divide 메서드 호출
	divideParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	divideResult, err := client.Divide(context.Background(), divideParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 / 5 = %.1f\n", divideResult) // 출력: 10 / 5 = 2.0
}

```

## 호환성 문제 해결

이 라이브러리는 Python의 jsonrpclib와 Go의 go-jsonrpc 간의 다음과 같은 차이점을 자동으로 해결합니다:

1. **메서드 이름 규칙**: Go 클라이언트에서는 메서드 이름을 지정할 때 다른 형식을 사용하므로, 이 라이브러리가 자동으로 해당 문제를 처리합니다.
2. **파라미터 처리**: 두 라이브러리 간의 파라미터 전달 방식 차이를 조정합니다.
3. **컨텍스트 처리**: Go의 컨텍스트 기반 호출을 Python 환경에서 적절히 처리합니다.

## 라이센스

MIT License