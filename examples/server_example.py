from easy_jsonrpc import EasyJSONRPCServer


def Hello(params):
    name = params.get("name", "World")
    return f"Hello, {name}!"


def Add(params):
    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    return a + b


if __name__ == "__main__":
    server = EasyJSONRPCServer("localhost", 8080, allow_go_client=True)
    server.register_function(Hello)
    server.register_function(Add)

    print("JSON-RPC 서버가 시작되었습니다.")
    print("호출 가능한 메서드:")
    print("- Hello")
    print("- Add")
    print("\nCtrl+C를 눌러 서버를 중지할 수 있습니다.")

    server.start()
