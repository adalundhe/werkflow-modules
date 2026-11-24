from __future__ import annotations
from pydantic import BaseModel
from .ec2_client_vpn_trust_provider import EC2ClientVpnTrustProvider


class EC2DevicePostureResponseOptions(BaseModel):
    TrustProviders: list[EC2ClientVpnTrustProvider] | None = None
