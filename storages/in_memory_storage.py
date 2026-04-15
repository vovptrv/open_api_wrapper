from typing import Any, Dict

from storages.storage_interface import Storage


class InMemoryStorage(Storage):
    """Simple dictionary-based storage."""

    def __init__(self) -> None:
        self._records: Dict[str, Any] = {}

    def create(self, key: str, payload: Any) -> None:
        self._records[key] = payload

    def read(self, key: str) -> Any:
        return self._records.get(key)

    def update(self, key: str, payload: Any) -> None:
        if key not in self._records:
            raise KeyError(key)
        self._records[key] = payload

    def delete(self, key: str) -> None:
        self._records.pop(key, None)

    def list_all(self) -> Dict[str, Any]:
        return self._records.copy()
