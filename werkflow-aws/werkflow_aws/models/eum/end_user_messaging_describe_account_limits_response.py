from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_account_limit import EndUserMessagingAccountLimit


class EndUserMessagingDescribeAccountLimitsResponse(BaseModel):
    AccountLimits: list[EndUserMessagingAccountLimit] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
