from easy_jsonrpc import EasyJSONRPCClient


def pytho_call():
    # 클라이언트 초기화
    client = EasyJSONRPCClient("http://localhost:8080")

    # hello 메서드 호출
    result = client.call("Hello", {"Name": "Alice", "Age": 20, "Message": "HI Hellow"})
    print(result)  # 출력: Hello, Alice!

    # add 메서드 호출
    sum_result = client.call("Add", {"A": 5, "B": 3})
    print(sum_result)  # 출력: 8

    # 알림 전송 (응답 기다리지 않음)
    client.notify("Hello", {"Name": "Alex", "Age": 25, "Message": "HI"})


def go_call():
    """
    GO 에서는 메서드앞에 스트럭트 명을 붙여야함
    """
    # 클라이언트 초기화
    client = EasyJSONRPCClient("http://localhost:8080")

    # HiHandler 스트럭트 Hello 메서드 호출
    result = client.call(
        "HiHandler.Hello", {"Name": "Alice", "Age": 20, "Message": "HI Hellow"}
    )
    print(result)  # 출력: Hello, Alice!

    # AddHandler 스트럭트 Add 메서드 호출
    sum_result = client.call("AddHandler.Add", {"A": 5, "B": 3})
    print(sum_result)  # 출력: 8

    # HiHandler 스트럭트 Hello 메서드 알림 전송 (응답 기다리지 않음)
    client.notify("HiHandler.Hello", {"Name": "Alex", "Age": 25, "Message": "HI"})


pytho_call()
go_call()
