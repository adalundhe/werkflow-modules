from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_account_settings import QuickSightAccountSettings


class QuickSightDescribeAccountSettingsResponse(BaseModel):
    AccountSettings: QuickSightAccountSettings | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
