from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_client_vpc_connection import MSKClientVpcConnection


class MSKListClientVpcConnectionsResponse(BaseModel):
    ClientVpcConnections: list[MSKClientVpcConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
