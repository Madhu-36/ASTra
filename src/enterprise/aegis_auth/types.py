from typing import TypeVar, Generic
T = TypeVar('T')
class EnterpriseResponse(Generic[T]):
    data: T
