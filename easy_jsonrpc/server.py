"""
JSON-RPC 서버 모듈

이 모듈은 Python과 Go 클라이언트 간의 호환성을 위한 JSON-RPC 서버를 제공합니다.
"""

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import inspect


class EasyJSONRPCServer:
    def __init__(self, host='localhost', port=8080, allow_go_client=True, allow_python_client=True):
        """
        JSON-RPC 서버 초기화
        
        Args:
            host (str): 바인딩할 IP 주소
            port (int): 바인딩할 포트
            allow_go_client (bool): Go 클라이언트 지원 여부
            allow_python_client (bool): Python 클라이언트 지원 여부
        """
        self.server = SimpleJSONRPCServer((host, port))
        self.go_client_support = allow_go_client
        self.python_client_support = allow_python_client
        self.methods = {}
        
        print("[SERVER] Initialized on {}:{}".format(host, port))
        print("[SERVER] Go client support: {}".format(allow_go_client))
        print("[SERVER] Python client support: {}".format(allow_python_client))
    
    def register_function(self, function, name=None, namespace=None):
        """
        함수를 JSON-RPC 서버에 등록
        
        Args:
            function (callable): 등록할 함수
            name (str, optional): 함수 이름 (기본값: 함수의 원래 이름)
            namespace (str, optional): 네임스페이스
            
        Returns:
            EasyJSONRPCServer: 메서드 체이닝을 위한 self
        """
        if name is None:
            name = function.__name__
            
        # 전체 메서드 이름 생성
        if namespace:
            full_name = "{}.{}".format(namespace, name)
        else:
            full_name = name
            
        # 내부 추적을 위해 저장
        self.methods[full_name] = function
        
        # Python 클라이언트를 위한 등록
        if self.python_client_support:
            self.server.register_function(function, full_name)
            print("[SERVER] Registered for Python clients: {}".format(full_name))
            
        # Go 클라이언트를 위한 등록
        if self.go_client_support:
            go_name = ".{}".format(full_name)
            self.server.register_function(function, go_name)
            print("[SERVER] Registered for Go clients: {}".format(go_name))
        
        return self
    
    def register_class(self, cls, namespace=None):
        """
        클래스의 모든 public 메서드를 등록
        
        Args:
            cls: 등록할 클래스 또는 인스턴스
            namespace (str, optional): 네임스페이스 (기본값: 클래스 이름)
            
        Returns:
            EasyJSONRPCServer: 메서드 체이닝을 위한 self
        """
        # 클래스가 인스턴스인지 확인
        if isinstance(cls, type):
            instance = cls()
            if namespace is None:
                namespace = cls.__name__
        else:
            instance = cls
            if namespace is None:
                namespace = cls.__class__.__name__
        
        # 클래스 내의 모든 public 메서드 찾기
        for name, method in inspect.getmembers(instance, predicate=inspect.ismethod):
            if not name.startswith('_'):  # private 메서드는 제외
                self.register_function(method, name, namespace)
        
        return self
        
    def start(self):
        """서버를 시작하고 요청 처리"""
        print("[SERVER] Starting with {} registered methods".format(len(self.methods)))
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("[SERVER] Stopping due to keyboard interrupt")
    
    def handle_request(self):
        """단일 요청만 처리"""
        self.server.handle_request() 