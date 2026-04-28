# Django settings module for mypy type checking (test configuration)
# This module is only used for mypy configuration and doesn't affect the actual application
from typing import Any, Dict, List

SECRET_KEY = "string"
INSTALLED_APPS: List[str] = []  # noqa: WPS407
DATABASES: Dict[str, Any] = {}  # noqa: WPS407
