from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ipam_cidr_authorization_context import EC2IpamCidrAuthorizationContext


class EC2ProvisionIpamPoolCidrRequest(BaseModel):
    IpamPoolId: StrictStr
    DryRun: StrictBool | None = None
    Cidr: StrictStr | None = None
    CidrAuthorizationContext: EC2IpamCidrAuthorizationContext | None = None
    NetmaskLength: StrictInt | None = None
    ClientToken: StrictStr | None = None
    VerificationMethod: Literal['remarks-x509', 'dns-token'] | None = None
    IpamExternalResourceVerificationTokenId: StrictStr | None = None
