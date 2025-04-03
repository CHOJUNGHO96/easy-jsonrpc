"""
JSON-RPC 클라이언트 모듈

이 모듈은 Python과 Go 서버 간의 호환성을 위한 JSON-RPC 클라이언트를 제공합니다.
"""

import jsonrpclib
import json


class EasyJSONRPCClient:
    def __init__(self, url, is_go_server=False):
        """
        JSON-RPC 클라이언트 초기화
        
        Args:
            url (str): 서버 URL (예: 'http://localhost:8080')
            is_go_server (bool): Go 서버 여부 (메서드 이름 처리 방식이 다름)
        """
        self.server = jsonrpclib.Server(url)
        self.url = url
        self.is_go_server = is_go_server
        print("[CLIENT] Connected to {}".format(url))
        print("[CLIENT] Go server compatibility mode: {}".format(is_go_server))
    
    def call(self, method, params=None, namespace=None):
        """
        양방향 RPC 호출 (응답 기다림)
        
        Args:
            method (str): 메서드 이름
            params (dict, optional): 파라미터
            namespace (str, optional): 네임스페이스
            
        Returns:
            응답 데이터
        """
        if params is None:
            params = {}
            
        # 전체 메서드 이름 생성
        if namespace:
            full_method = "{}.{}".format(namespace, method)
        else:
            full_method = method
            
        # Go 서버를 위한 조정
        if self.is_go_server:
            if not full_method.startswith('.'):
                full_method = ".{}".format(full_method)
        
        print("[CLIENT] Calling {} with params: {}".format(full_method, params))
        
        try:
            # 동적 메서드 호출 (점 표기법을 지원하기 위한 처리)
            if '.' in full_method and not full_method.startswith('.'):
                parts = full_method.split('.')
                obj = self.server
                for part in parts[:-1]:
                    obj = getattr(obj, part)
                method_to_call = getattr(obj, parts[-1])
            else:
                method_to_call = getattr(self.server, full_method)
                
            result = method_to_call(params)
            return result
        except Exception as e:
            print("[CLIENT] Error calling {}: {}".format(full_method, e))
            raise
    
    def notify(self, method, params=None, namespace=None):
        """
        단방향 알림 전송 (응답 기다리지 않음)
        
        Args:
            method (str): 메서드 이름
            params (dict, optional): 파라미터
            namespace (str, optional): 네임스페이스
        """
        if params is None:
            params = {}
            
        # 전체 메서드 이름 생성
        if namespace:
            full_method = "{}.{}".format(namespace, method)
        else:
            full_method = method
        
        # Go 서버를 위한 조정
        if self.is_go_server and not full_method.startswith('.'):
            full_method = ".{}".format(full_method)
            
        print("[CLIENT] Sending notification to {} with params: {}".format(full_method, params))
        
        # JSON-RPC 2.0 알림 형식 (id 없음)
        request = {
            "jsonrpc": "2.0",
            "method": full_method,
            "params": [params]  # 파라미터를 배열로 감싸기
        }
        
        request_body = json.dumps(request).encode('utf-8')
        
        try:
            # 내부 메서드 호출하여 전송
            response = self.server._ServerProxy__transport.request(
                self.server._ServerProxy__host,
                self.server._ServerProxy__handler,
                request_body
            )
            print("[CLIENT] Notification sent: {}".format(response))
        except Exception as e:
            print("[CLIENT] Error sending notification to {}: {}".format(full_method, e))
            raise 