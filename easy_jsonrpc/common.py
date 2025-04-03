"""
JSON-RPC 공통 유틸리티 모듈

이 모듈은 JSON-RPC 클라이언트와 서버에서 공통으로 사용하는 유틸리티 함수를 제공합니다.
"""


def convert_params(params):
    """
    매개변수 변환 도우미 함수 (Python 3.5 호환성 보장)
    
    다양한 형식의 매개변수를 JSON-RPC 요청에 적합한 형태로 변환합니다.
    
    Args:
        params: 변환할 매개변수 (None, 단일 값, 사전, 리스트 등)
        
    Returns:
        dict: 변환된 매개변수 사전
    """
    if isinstance(params, dict):
        return params
    elif params is None:
        return {}
    elif isinstance(params, (list, tuple)):
        return {"args": params}
    else:
        return {"value": params}


def format_error(error_code, message, data=None):
    """
    JSON-RPC 오류 형식을 생성하는 함수
    
    Args:
        error_code (int): 오류 코드
        message (str): 오류 메시지
        data (any, optional): 추가 오류 데이터
        
    Returns:
        dict: JSON-RPC 오류 형식
    """
    error = {
        "code": error_code,
        "message": message
    }
    
    if data is not None:
        error["data"] = data
        
    return {"error": error}


# 표준 JSON-RPC 오류 코드
PARSE_ERROR = -32700
INVALID_REQUEST = -32600
METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603 