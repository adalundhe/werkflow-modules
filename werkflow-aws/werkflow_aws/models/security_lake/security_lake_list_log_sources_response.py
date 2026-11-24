from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_lake_log_source import SecurityLakeLogSource


class SecurityLakeListLogSourcesResponse(BaseModel):
    nextToken: StrictStr | None = None
    sources: list[SecurityLakeLogSource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
