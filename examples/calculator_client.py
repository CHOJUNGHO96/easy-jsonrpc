from easy_jsonrpc import EasyJSONRPCClient


def main():
    client = EasyJSONRPCClient("http://localhost:8080")

    try:
        add_result = client.call("Calculator.Add", {"a": 10, "b": 5})
        print(f"10 + 5 = {add_result}")
    except Exception as e:
        print(f"Add 호출 중 오류 발생: {e}")

    try:
        subtract_result = client.call("Calculator.Subtract", {"a": 10, "b": 5})
        print(f"10 - 5 = {subtract_result}")
    except Exception as e:
        print(f"Subtract 호출 중 오류 발생: {e}")

    try:
        multiply_result = client.call("Calculator.Multiply", {"a": 10, "b": 5})
        print(f"10 * 5 = {multiply_result}")
    except Exception as e:
        print(f"Multiply 호출 중 오류 발생: {e}")

    try:
        divide_result = client.call("Calculator.Divide", {"a": 10, "b": 5})
        print(f"10 / 5 = {divide_result}")
    except Exception as e:
        print(f"Divide 호출 중 오류 발생: {e}")

    try:
        client.notify("Calculator.Add", {"a": 10, "b": 5})
        print(f"알림보내기 완료")
    except Exception as e:
        print(f"Add 호출 중 오류 발생: {e}")


if __name__ == "__main__":
    main()
