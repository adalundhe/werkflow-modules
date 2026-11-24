from __future__ import annotations
from pydantic import BaseModel
from .eks_addon import EKSAddon


class EKSDeleteAddonResponse(BaseModel):
    addon: EKSAddon | None = None
