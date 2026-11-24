from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_lake_custom_log_source_resource import SecurityLakeCustomLogSourceResource


class SecurityLakeCreateCustomLogSourceResponse(BaseModel):
    source: SecurityLakeCustomLogSourceResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
