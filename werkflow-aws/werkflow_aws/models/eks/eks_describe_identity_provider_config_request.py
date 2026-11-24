from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_identity_provider_config import EKSIdentityProviderConfig


class EKSDescribeIdentityProviderConfigRequest(BaseModel):
    clusterName: StrictStr
    identityProviderConfig: EKSIdentityProviderConfig
