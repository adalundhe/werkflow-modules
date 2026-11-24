from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool


class MacieDescribeOrganizationConfigurationResponse(BaseModel):
    autoEnable: StrictBool | None = None
    maxAccountLimitReached: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
