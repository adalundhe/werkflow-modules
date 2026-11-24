from __future__ import annotations
from pydantic import BaseModel
from .eks_update import EKSUpdate


class EKSUpdateClusterConfigResponse(BaseModel):
    update: EKSUpdate | None = None
