from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_connection_status import EC2ClientVpnConnectionStatus


class EC2TerminateConnectionStatus(BaseModel):
    ConnectionId: StrictStr | None = None
    PreviousStatus: EC2ClientVpnConnectionStatus | None = None
    CurrentStatus: EC2ClientVpnConnectionStatus | None = None
