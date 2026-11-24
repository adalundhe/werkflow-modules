from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_modify_vpn_tunnel_options_specification import EC2ModifyVpnTunnelOptionsSpecification


class EC2ModifyVpnTunnelOptionsRequest(BaseModel):
    VpnConnectionId: StrictStr
    VpnTunnelOutsideIpAddress: StrictStr
    TunnelOptions: EC2ModifyVpnTunnelOptionsSpecification
    DryRun: StrictBool | None = None
    SkipTunnelReplacement: StrictBool | None = None
    PreSharedKeyStorage: StrictStr | None = None
