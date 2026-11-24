from __future__ import annotations
from pydantic import BaseModel
from .batch_eks_pod_properties_detail import BatchEksPodPropertiesDetail


class BatchEksPropertiesDetail(BaseModel):
    podProperties: BatchEksPodPropertiesDetail | None = None
