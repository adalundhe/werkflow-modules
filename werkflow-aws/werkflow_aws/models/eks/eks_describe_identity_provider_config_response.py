from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_identity_provider_config_response import EKSIdentityProviderConfigResponse


class EKSDescribeIdentityProviderConfigResponse(BaseModel):
    identityProviderConfig: EKSIdentityProviderConfigResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
