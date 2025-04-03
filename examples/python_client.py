from easy_jsonrpc import EasyJSONRPCClient


def main():
    client = EasyJSONRPCClient("http://localhost:8080", is_go_server=True)

    try:
        result = client.call("Hello", {"name": "Alice"})
        print(f"Hello 호출 결과: {result}")
    except Exception as e:
        print(f"Hello 호출 중 오류 발생: {e}")

    try:
        sum_result = client.call("Add", {"a": 5, "b": 3})
        print(f"Add 호출 결과: {sum_result}")
    except Exception as e:
        print(f"Add 호출 중 오류 발생: {e}")

    try:
        client.notify("Hello", {"name": "Notification"})
        print("알림 전송 완료")
    except Exception as e:
        print(f"알림 전송 중 오류 발생: {e}")


if __name__ == "__main__":
    main()
