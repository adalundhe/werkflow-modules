from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBDescribeServiceUpdatesRequest(BaseModel):
    ServiceUpdateName: StrictStr | None = None
    ClusterNames: list[StrictStr] | None = None
    Status: list[Literal['available', 'in-progress', 'complete', 'scheduled']] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
