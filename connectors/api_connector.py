from abc import ABC, abstractmethod
from typing import Any, Dict


class ApiConnector(ABC):
    """Base interface for API connectors."""

    @abstractmethod
    def get(
        self,
        endpoint: str,
        query_params: Dict[str, Any],
    ) -> Dict[str, Any]: ...
