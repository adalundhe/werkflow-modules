from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_oidc_identity_provider_config_request import EKSOidcIdentityProviderConfigRequest


class EKSAssociateIdentityProviderConfigRequest(BaseModel):
    clusterName: StrictStr
    oidc: EKSOidcIdentityProviderConfigRequest
    tags: dict[StrictStr, StrictStr] | None = None
    clientRequestToken: StrictStr | None = None
