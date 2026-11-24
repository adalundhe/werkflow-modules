from __future__ import annotations
from pydantic import BaseModel
from .batch_eks_pod_properties_override import BatchEksPodPropertiesOverride


class BatchEksPropertiesOverride(BaseModel):
    podProperties: BatchEksPodPropertiesOverride | None = None
