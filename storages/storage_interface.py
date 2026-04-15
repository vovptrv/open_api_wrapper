from abc import ABC, abstractmethod
from typing import Any, Dict


class Storage(ABC):
    """Abstract storage interface."""

    @abstractmethod
    def create(self, key: str, payload: Any) -> None: ...

    @abstractmethod
    def read(self, key: str) -> Any: ...

    @abstractmethod
    def update(self, key: str, payload: Any) -> None: ...

    @abstractmethod
    def delete(self, key: str) -> None: ...

    @abstractmethod
    def list_all(self) -> Dict[str, Any]: ...
