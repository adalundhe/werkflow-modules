from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_connection_status import EC2ClientVpnConnectionStatus


class EC2ClientVpnConnection(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Timestamp: StrictStr | None = None
    ConnectionId: StrictStr | None = None
    Username: StrictStr | None = None
    ConnectionEstablishedTime: StrictStr | None = None
    IngressBytes: StrictStr | None = None
    EgressBytes: StrictStr | None = None
    IngressPackets: StrictStr | None = None
    EgressPackets: StrictStr | None = None
    ClientIp: StrictStr | None = None
    ClientIpv6Address: StrictStr | None = None
    CommonName: StrictStr | None = None
    Status: EC2ClientVpnConnectionStatus | None = None
    ConnectionEndTime: StrictStr | None = None
    PostureComplianceStatuses: list[StrictStr] | None = None
    AuthorizationPolicyLastEvaluatedTime: StrictStr | None = None
