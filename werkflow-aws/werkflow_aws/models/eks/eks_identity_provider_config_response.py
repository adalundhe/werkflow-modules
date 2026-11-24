from __future__ import annotations
from pydantic import BaseModel
from .eks_oidc_identity_provider_config import EKSOidcIdentityProviderConfig


class EKSIdentityProviderConfigResponse(BaseModel):
    oidc: EKSOidcIdentityProviderConfig | None = None
