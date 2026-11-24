from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_spend_limit import EndUserMessagingSpendLimit


class EndUserMessagingDescribeSpendLimitsResponse(BaseModel):
    SpendLimits: list[EndUserMessagingSpendLimit] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
