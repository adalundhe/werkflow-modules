from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_pool_information import EndUserMessagingPoolInformation


class EndUserMessagingDescribePoolsResponse(BaseModel):
    Pools: list[EndUserMessagingPoolInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
