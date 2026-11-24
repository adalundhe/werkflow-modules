from __future__ import annotations
from pydantic import BaseModel
from .eks_nodegroup import EKSNodegroup


class EKSCreateNodegroupResponse(BaseModel):
    nodegroup: EKSNodegroup | None = None
