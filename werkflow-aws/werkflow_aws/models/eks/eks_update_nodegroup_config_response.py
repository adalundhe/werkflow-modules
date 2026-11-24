from __future__ import annotations
from pydantic import BaseModel
from .eks_update import EKSUpdate


class EKSUpdateNodegroupConfigResponse(BaseModel):
    update: EKSUpdate | None = None
