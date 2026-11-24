from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_monitoring_cluster_config import SageMakerMonitoringClusterConfig


class SageMakerMonitoringResources(BaseModel):
    ClusterConfig: SageMakerMonitoringClusterConfig | None = None
