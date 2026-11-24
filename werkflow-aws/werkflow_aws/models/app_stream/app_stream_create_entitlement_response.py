from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_entitlement import AppStreamEntitlement


class AppStreamCreateEntitlementResponse(BaseModel):
    Entitlement: AppStreamEntitlement | None = None
    ResponseMetadata: dict[str, Any] | None = None
