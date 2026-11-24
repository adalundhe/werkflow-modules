from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_instance_open_vpn_client_configuration_route import EC2VerifiedAccessInstanceOpenVpnClientConfigurationRoute


class EC2VerifiedAccessInstanceOpenVpnClientConfiguration(BaseModel):
    Config: StrictStr | None = None
    Routes: list[EC2VerifiedAccessInstanceOpenVpnClientConfigurationRoute] | None = None
