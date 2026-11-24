from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_engine_version_info import MemoryDBEngineVersionInfo


class MemoryDBDescribeEngineVersionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    EngineVersions: list[MemoryDBEngineVersionInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
