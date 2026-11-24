from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .direct_connect_resiliency_group import DirectConnectResiliencyGroup


class DirectConnectDeleteResiliencyGroupResponse(BaseModel):
    resiliencyGroup: DirectConnectResiliencyGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
