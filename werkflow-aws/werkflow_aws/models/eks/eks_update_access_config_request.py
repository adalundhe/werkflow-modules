from __future__ import annotations
from pydantic import BaseModel
from .eks_authentication_mode import EKSAuthenticationMode


class EKSUpdateAccessConfigRequest(BaseModel):
    authenticationMode: EKSAuthenticationMode | None = None
