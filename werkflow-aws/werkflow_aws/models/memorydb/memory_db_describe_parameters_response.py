from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_parameter import MemoryDBParameter


class MemoryDBDescribeParametersResponse(BaseModel):
    NextToken: StrictStr | None = None
    Parameters: list[MemoryDBParameter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
