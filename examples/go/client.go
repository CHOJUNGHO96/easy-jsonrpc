// go 클라이언트 예제
// 실행을 위해서는 먼저 필요한 패키지를 설치해야 합니다:
// go get github.com/filecoin-project/go-jsonrpc

package main

import (
	"context"
	"fmt"
	"time"

	"github.com/filecoin-project/go-jsonrpc"
)

// API 인터페이스 정의
type API interface {
	ScanStarted(ctx context.Context, params map[string]interface{}) (bool, error)
	TestFunction(ctx context.Context, params map[string]interface{}) (interface{}, error)
	Echo(ctx context.Context, params map[string]interface{}) (interface{}, error)
}

// SimpleServerHandler 네임스페이스용 인터페이스
type SimpleServerHandlerAPI interface {
	AddGet(ctx context.Context, params map[string]interface{}) (int, error)
}

func main() {
	fmt.Println("=== JSON-RPC Go 클라이언트 예제 ===")

	// 1. API 클라이언트 생성
	fmt.Println("\n일반 메서드 호출 예제:")
	var client API
	closer, err := jsonrpc.NewClient(context.Background(), "http://localhost:9090", "", &client, nil)
	if err != nil {
		panic(err)
	}
	defer closer()

	// ScanStarted 메서드 호출
	scanParams := map[string]interface{}{
		"file_path": "/tmp/go_client_test.exe",
	}
	scanResult, err := client.ScanStarted(context.Background(), scanParams)
	if err != nil {
		fmt.Printf("ScanStarted 호출 오류: %s\n", err)
	} else {
		fmt.Printf("ScanStarted 결과: %v\n", scanResult)
	}

	// TestFunction 메서드 호출
	testParams := map[string]interface{}{
		"value": 100,
	}
	testResult, err := client.TestFunction(context.Background(), testParams)
	if err != nil {
		fmt.Printf("TestFunction 호출 오류: %s\n", err)
	} else {
		fmt.Printf("TestFunction 결과: %v\n", testResult)
	}

	// Echo 메서드 호출 (TestFunction의 별칭)
	echoParams := map[string]interface{}{
		"value": "Hello from Go!",
	}
	echoResult, err := client.Echo(context.Background(), echoParams)
	if err != nil {
		fmt.Printf("Echo 호출 오류: %s\n", err)
	} else {
		fmt.Printf("Echo 결과: %v\n", echoResult)
	}

	// 2. SimpleServerHandler 네임스페이스 메서드 호출
	fmt.Println("\nSimpleServerHandler 네임스페이스 메서드 호출 예제:")
	time.Sleep(1 * time.Second) // 잠시 대기

	var handlerClient SimpleServerHandlerAPI
	handlerCloser, err := jsonrpc.NewClient(context.Background(), "http://localhost:9090", "SimpleServerHandler", &handlerClient, nil)
	if err != nil {
		panic(err)
	}
	defer handlerCloser()

	// AddGet 메서드 호출
	addParams := map[string]interface{}{
		"a": 30,
		"b": 12,
	}
	addResult, err := handlerClient.AddGet(context.Background(), addParams)
	if err != nil {
		fmt.Printf("SimpleServerHandler.AddGet 호출 오류: %s\n", err)
	} else {
		fmt.Printf("SimpleServerHandler.AddGet 결과: %v\n", addResult)
	}
}
