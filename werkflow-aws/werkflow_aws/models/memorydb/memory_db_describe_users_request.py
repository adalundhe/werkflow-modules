from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .memory_db_filter import MemoryDBFilter


class MemoryDBDescribeUsersRequest(BaseModel):
    UserName: StrictStr | None = None
    Filters: list[MemoryDBFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
