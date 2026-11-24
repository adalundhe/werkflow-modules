from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .eks_authentication_mode import EKSAuthenticationMode


class EKSCreateAccessConfigRequest(BaseModel):
    bootstrapClusterCreatorAdminPermissions: StrictBool | None = None
    authenticationMode: EKSAuthenticationMode | None = None
