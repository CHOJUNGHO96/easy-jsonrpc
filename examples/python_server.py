from easy_jsonrpc import EasyJSONRPCServer

# 간단한 함수 정의
def hello(params):
    name = params.get("name", "World")
    return f"Hello, {name}!"

def add(params):
    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    return a + b

# 서버 초기화 및 실행
server = EasyJSONRPCServer('localhost', 8080, allow_go_client=True)
server.register_function(hello, 'Hello')
server.register_function(add, 'Add')
server.start()