from __future__ import annotations
from pydantic import BaseModel
from .eks_nodegroup import EKSNodegroup


class EKSDeleteNodegroupResponse(BaseModel):
    nodegroup: EKSNodegroup | None = None
