from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_client_vpn_trust_provider_request import EC2ClientVpnTrustProviderRequest


class EC2DevicePostureOptions(BaseModel):
    TrustProviders: list[EC2ClientVpnTrustProviderRequest] | None = None
    Enabled: StrictBool | None = None
