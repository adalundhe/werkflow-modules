from __future__ import annotations
from pydantic import BaseModel
from .eks_taint import EKSTaint


class EKSUpdateTaintsPayload(BaseModel):
    addOrUpdateTaints: list[EKSTaint] | None = None
    removeTaints: list[EKSTaint] | None = None
