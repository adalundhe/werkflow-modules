from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_asn_authorization_context import EC2AsnAuthorizationContext


class EC2ProvisionIpamByoasnRequest(BaseModel):
    IpamId: StrictStr
    Asn: StrictStr
    AsnAuthorizationContext: EC2AsnAuthorizationContext
    DryRun: StrictBool | None = None
