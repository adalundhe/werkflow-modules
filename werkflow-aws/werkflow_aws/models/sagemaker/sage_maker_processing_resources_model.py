from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_processing_cluster_config_model import SageMakerProcessingClusterConfigModel


class SageMakerProcessingResourcesModel(BaseModel):
    ClusterConfig: SageMakerProcessingClusterConfigModel | None = None
