from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .direct_connect_connection import DirectConnectConnection


class DirectConnectUpdateConnectionsBillingModeResponse(BaseModel):
    billingMode: StrictStr | None = None
    connections: list[DirectConnectConnection] | None = None
    ResponseMetadata: dict[str, Any] | None = None
