from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_trust_provider import EC2VerifiedAccessTrustProvider


class EC2DescribeVerifiedAccessTrustProvidersResponse(BaseModel):
    VerifiedAccessTrustProviders: list[EC2VerifiedAccessTrustProvider] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
