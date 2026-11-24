from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .security_hub_aws_ec2_vpn_connection_options_tunnel_options_details import SecurityHubAwsEc2VpnConnectionOptionsTunnelOptionsDetails


class SecurityHubAwsEc2VpnConnectionOptionsDetails(BaseModel):
    StaticRoutesOnly: StrictBool | None = None
    TunnelOptions: list[SecurityHubAwsEc2VpnConnectionOptionsTunnelOptionsDetails] | None = None
