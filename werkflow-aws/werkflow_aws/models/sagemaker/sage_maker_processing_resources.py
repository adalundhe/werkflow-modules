from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_processing_cluster_config import SageMakerProcessingClusterConfig


class SageMakerProcessingResources(BaseModel):
    ClusterConfig: SageMakerProcessingClusterConfig | None = None
