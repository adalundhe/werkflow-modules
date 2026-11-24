from __future__ import annotations
from pydantic import BaseModel
from .eks_block_storage import EKSBlockStorage


class EKSStorageConfigRequest(BaseModel):
    blockStorage: EKSBlockStorage | None = None
