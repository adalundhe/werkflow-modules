from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_verified_access_trust_provider import EC2VerifiedAccessTrustProvider


class EC2CreateVerifiedAccessTrustProviderResponse(BaseModel):
    VerifiedAccessTrustProvider: EC2VerifiedAccessTrustProvider | None = None
    ResponseMetadata: dict[str, Any] | None = None
