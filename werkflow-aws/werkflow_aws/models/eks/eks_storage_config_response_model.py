from __future__ import annotations
from pydantic import BaseModel
from .eks_block_storage_model import EKSBlockStorageModel


class EKSStorageConfigResponseModel(BaseModel):
    blockStorage: EKSBlockStorageModel | None = None
