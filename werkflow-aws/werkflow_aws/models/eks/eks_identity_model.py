from __future__ import annotations
from pydantic import BaseModel
from .eksoidc_model import EKSOIDCModel


class EKSIdentityModel(BaseModel):
    oidc: EKSOIDCModel | None = None
