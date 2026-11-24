from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_multi_region_parameter import MemoryDBMultiRegionParameter


class MemoryDBDescribeMultiRegionParametersResponse(BaseModel):
    NextToken: StrictStr | None = None
    MultiRegionParameters: list[MemoryDBMultiRegionParameter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
