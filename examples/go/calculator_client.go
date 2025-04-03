package main

import (
	"context"
	"fmt"

	"github.com/filecoin-project/go-jsonrpc"
)

func main() {
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

	addParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	addResult, err := client.Add(context.Background(), addParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 + 5 = %d\n", addResult)

	subtractParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	subtractResult, err := client.Subtract(context.Background(), subtractParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 - 5 = %d\n", subtractResult)

	multiplyParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	multiplyResult, err := client.Multiply(context.Background(), multiplyParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 * 5 = %d\n", multiplyResult)

	divideParams := map[string]interface{}{
		"a": 10,
		"b": 5,
	}
	divideResult, err := client.Divide(context.Background(), divideParams)
	if err != nil {
		panic(err)
	}
	fmt.Printf("10 / 5 = %.1f\n", divideResult)
}
