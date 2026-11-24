from __future__ import annotations
from pydantic import BaseModel
from .batch_eks_container_override import BatchEksContainerOverride
from .batch_eks_metadata import BatchEksMetadata


class BatchEksPodPropertiesOverride(BaseModel):
    containers: list[BatchEksContainerOverride] | None = None
    initContainers: list[BatchEksContainerOverride] | None = None
    metadata: BatchEksMetadata | None = None
