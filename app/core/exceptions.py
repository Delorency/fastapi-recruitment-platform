from typing import Any, Dict, Optional

from fastapi import HTTPException, status



class ServerSideError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_500_INTERNAL_SERVER_ERROR, detail, headers)


class BadRequestError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class NotFoundError(HTTPException):
	def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
		super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class AuthError(HTTPException):
	def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
		super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)


class UnauthorizedError(HTTPException):
	def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
		super().__init__(status.HTTP_401_UNAUHORIZED, detail, headers)