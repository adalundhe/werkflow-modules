from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class EC2DeleteVpnConnectionRouteResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
