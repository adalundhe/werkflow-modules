from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_terminate_connection_status import EC2TerminateConnectionStatus


class EC2TerminateClientVpnConnectionsResponse(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Username: StrictStr | None = None
    ConnectionStatuses: list[EC2TerminateConnectionStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
