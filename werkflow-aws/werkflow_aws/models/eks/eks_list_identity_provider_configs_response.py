from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_identity_provider_config import EKSIdentityProviderConfig


class EKSListIdentityProviderConfigsResponse(BaseModel):
    identityProviderConfigs: list[EKSIdentityProviderConfig] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
