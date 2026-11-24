from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_external_resource_verification_token import EC2IpamExternalResourceVerificationToken


class EC2DescribeIpamExternalResourceVerificationTokensResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamExternalResourceVerificationTokens: list[EC2IpamExternalResourceVerificationToken] | None = None
    ResponseMetadata: dict[str, Any] | None = None
