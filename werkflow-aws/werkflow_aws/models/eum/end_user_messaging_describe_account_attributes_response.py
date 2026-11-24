from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_account_attribute import EndUserMessagingAccountAttribute


class EndUserMessagingDescribeAccountAttributesResponse(BaseModel):
    AccountAttributes: list[EndUserMessagingAccountAttribute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
