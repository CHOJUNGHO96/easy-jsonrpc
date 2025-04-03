from easy_jsonrpc import EasyJSONRPCClient

# 클라이언트 초기화
client = EasyJSONRPCClient('http://localhost:9090')

# Calculator 클래스의 메서드 호출
add_result = client.call('Calculator.add', {"a": 10, "b": 5})
print(f"10 + 5 = {add_result}")  # 출력: 10 + 5 = 15

subtract_result = client.call('Calculator.subtract', {"a": 10, "b": 5})
print(f"10 - 5 = {subtract_result}")  # 출력: 10 - 5 = 5

multiply_result = client.call('Calculator.multiply', {"a": 10, "b": 5})
print(f"10 * 5 = {multiply_result}")  # 출력: 10 * 5 = 50

divide_result = client.call('Calculator.divide', {"a": 10, "b": 5})
print(f"10 / 5 = {divide_result}")  # 출력: 10 / 5 = 2.0