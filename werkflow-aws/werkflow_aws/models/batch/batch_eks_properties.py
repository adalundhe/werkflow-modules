from __future__ import annotations
from pydantic import BaseModel
from .batch_eks_pod_properties import BatchEksPodProperties


class BatchEksProperties(BaseModel):
    podProperties: BatchEksPodProperties | None = None
