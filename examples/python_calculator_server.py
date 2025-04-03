from easy_jsonrpc import EasyJSONRPCServer


# 클래스 정의
class Calculator:
    def add(self, params):
        a = params.get("a", 0)
        b = params.get("b", 0)
        return a + b

    def subtract(self, params):
        a = params.get("a", 0)
        b = params.get("b", 0)
        return a - b

    def multiply(self, params):
        a = params.get("a", 0)
        b = params.get("b", 0)
        return a * b


# 서버 초기화 및 클래스 등록
server = EasyJSONRPCServer('localhost', 9090)
server.register_class(Calculator)  # Calculator의 모든 메서드 등록
server.start()