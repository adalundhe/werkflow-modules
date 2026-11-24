from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_reserved_instance import OpenSearchReservedInstance


class OpenSearchDescribeReservedInstancesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ReservedInstances: list[OpenSearchReservedInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
