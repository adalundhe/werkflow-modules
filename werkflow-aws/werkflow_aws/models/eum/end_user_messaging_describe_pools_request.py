from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_pool_filter import EndUserMessagingPoolFilter


class EndUserMessagingDescribePoolsRequest(BaseModel):
    PoolIds: list[StrictStr] | None = None
    Filters: list[EndUserMessagingPoolFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Owner: Literal['SELF', 'SHARED'] | None = None
