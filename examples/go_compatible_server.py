#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Go 클라이언트와 호환되는 JSON-RPC 서버 예제

이 예제는 Go 클라이언트에서 호출할 수 있는 JSON-RPC 서버를 생성합니다.
"""

from easy_jsonrpc import EasyJSONRPCServer


# Hello 함수 구현
def hello(params):
    """
    인사말을 반환합니다.

    Args:
        params (dict): 요청 파라미터 ('name' 포함)

    Returns:
        str: 인사말 메시지
    """
    name = params.get("name", "World")
    return f"Hello, {name}!"


# Add 함수 구현
def add(params):
    """
    두 수를 더한 결과를 반환합니다.

    Args:
        params (dict): 요청 파라미터 ('a'와 'b' 포함)

    Returns:
        int: 두 수의 합
    """
    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    return a + b


if __name__ == "__main__":
    # JSON-RPC 서버 생성
    server = EasyJSONRPCServer(host="localhost", port=8080)

    # Go 클라이언트와 호환되는 함수 등록
    # 참고: Go 클라이언트는 함수를 스트럭트 필드로 호출하므로, 같은 이름으로 등록해야 함
    server.register_function(hello, "Hello")
    server.register_function(add, "Add")

    print("Starting JSON-RPC server for Go client compatibility...")
    print("Registered methods:")
    print("- Hello")
    print("- Add")
    print("\nPress Ctrl+C to stop the server")

    # 서버 시작
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer stopped")
