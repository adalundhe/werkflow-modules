from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_entitlement import AppStreamEntitlement


class AppStreamDescribeEntitlementsResponse(BaseModel):
    Entitlements: list[AppStreamEntitlement] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
