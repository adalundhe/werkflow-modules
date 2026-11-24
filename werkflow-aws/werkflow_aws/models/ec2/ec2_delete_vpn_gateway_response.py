from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class EC2DeleteVpnGatewayResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
