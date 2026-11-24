from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_routing_profile import ConnectRoutingProfile


class ConnectDescribeRoutingProfileResponse(BaseModel):
    RoutingProfile: ConnectRoutingProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
