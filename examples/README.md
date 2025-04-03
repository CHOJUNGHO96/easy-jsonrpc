# Easy-JSONRPC 예제 모음

이 디렉토리에는 easy-jsonrpc 라이브러리를 사용하는 다양한 예제가 포함되어 있습니다.

## Python 예제

### 1. 서버 예제

- `server_example.py`: 간단한 함수를 정의하고 JSON-RPC 서버에 등록하는 예제
  - `Hello` 함수와 `Add` 함수를 제공하는 서버
  - 실행 방법: `python server_example.py`

### 2. Python 클라이언트 예제

- `python_client.py`: Python 클라이언트에서 서버의 함수를 호출하는 예제
  - `Hello` 함수와 `Add` 함수를 호출
  - 실행 방법: `python python_client.py`

### 3. Calculator 서버 예제

- `calculator_server.py`: Calculator 클래스의 메서드를 제공하는 서버 예제
  - `Add`, `Subtract`, `Multiply`, `Divide` 메서드 제공
  - 실행 방법: `python calculator_server.py`

### 4. Calculator 클라이언트 예제

- `calculator_client.py`: Python 클라이언트에서 Calculator 클래스의 메서드를 호출하는 예제
  - 실행 방법: `python calculator_client.py`

## Go 예제

Go 클라이언트 예제를 실행하기 위해서는 먼저 필요한 패키지를 설치해야 합니다:

```bash
# go-jsonrpc 패키지 설치
go get github.com/filecoin-project/go-jsonrpc
```

### 1. 간단한 함수 호출 예제

- `go/function_client.go`: Go 클라이언트에서 서버의 함수를 호출하는 예제
  - `Hello` 함수와 `Add` 함수를 호출
  - 빌드 및 실행 방법:
    ```bash
    cd go
    go build function_client.go
    ./function_client
    ```

### 2. Calculator 클라이언트 예제

- `go/calculator_client.go`: Go 클라이언트에서 Calculator 클래스의 메서드를 호출하는 예제
  - 빌드 및 실행 방법:
    ```bash
    cd go
    go build calculator_client.go
    ./calculator_client
    ```

## 사용 시나리오 예제

### 시나리오 1: Python 서버와 Python 클라이언트

1. Python 서버 실행: `python server_example.py`
2. 다른 터미널에서 Python 클라이언트 실행: `python python_client.py`

### 시나리오 2: Python 서버와 Go 클라이언트

1. Python 서버 실행: `python server_example.py`
2. 다른 터미널에서 Go 클라이언트 실행: `cd go && go run function_client.go`

### 시나리오 3: Calculator 서버와 Python/Go 클라이언트

1. Calculator 서버 실행: `python calculator_server.py`
2. Python 클라이언트 실행: `python calculator_client.py`
3. 또는 Go 클라이언트 실행: `cd go && go run calculator_client.go`

## 주의사항

- Go 클라이언트와 통신하려면 Python 서버에서 함수/메서드 이름을 **반드시 UpperCamelCase**로 정의해야 합니다.
- Calculator 클래스 메서드를 호출할 때는 Go 클라이언트에서 네임스페이스를 올바르게 지정해야 합니다. 