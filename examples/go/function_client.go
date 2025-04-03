package main

import (
	"context"
	"fmt"

	"github.com/filecoin-project/go-jsonrpc"
)

func main() {
	var client struct {
		Hello func(ctx context.Context, params map[string]interface{}) (string, error)
		Add   func(ctx context.Context, params map[string]interface{}) (int, error)
	}

	closer, err := jsonrpc.NewClient(context.Background(), "http://localhost:8080", "", &client, nil)
	if err != nil {
		panic(err)
	}
	defer closer()

	params := map[string]interface{}{
		"name": "Bob",
	}
	result, err := client.Hello(context.Background(), params)
	if err != nil {
		panic(err)
	}
	fmt.Println(result)

	addParams := map[string]interface{}{
		"a": 10,
		"b": 20,
	}
	sum, err := client.Add(context.Background(), addParams)
	if err != nil {
		panic(err)
	}
	fmt.Println("Sum:", sum)
}
