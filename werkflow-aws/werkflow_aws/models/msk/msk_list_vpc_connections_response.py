from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_vpc_connection import MSKVpcConnection


class MSKListVpcConnectionsResponse(BaseModel):
    VpcConnections: list[MSKVpcConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
