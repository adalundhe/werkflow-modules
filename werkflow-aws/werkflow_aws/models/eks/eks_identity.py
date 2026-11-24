from __future__ import annotations
from pydantic import BaseModel
from .eksoidc import EKSOIDC


class EKSIdentity(BaseModel):
    oidc: EKSOIDC | None = None
