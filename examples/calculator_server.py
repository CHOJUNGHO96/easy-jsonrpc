from easy_jsonrpc import EasyJSONRPCServer


class Calculator:
    def Add(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a + b

    def Subtract(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a - b

    def Multiply(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 0))
        return a * b

    def Divide(self, params):
        a = int(params.get("a", 0))
        b = int(params.get("b", 1))
        if b == 0:
            return "Error: Division by zero"
        return a / b


if __name__ == "__main__":
    server = EasyJSONRPCServer("localhost", 8080, allow_go_client=True)
    server.register_class(Calculator)

    print("Calculator 서버가 시작되었습니다.")
    print("호출 가능한 메서드:")
    print("- Calculator.Add")
    print("- Calculator.Subtract")
    print("- Calculator.Multiply")
    print("- Calculator.Divide")
    print("\nCtrl+C를 눌러 서버를 중지할 수 있습니다.")

    server.start()
