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