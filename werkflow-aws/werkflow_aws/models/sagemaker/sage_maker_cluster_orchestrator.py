from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cluster_orchestrator_eks_config import SageMakerClusterOrchestratorEksConfig
from .sage_maker_cluster_orchestrator_slurm_config import SageMakerClusterOrchestratorSlurmConfig


class SageMakerClusterOrchestrator(BaseModel):
    Eks: SageMakerClusterOrchestratorEksConfig | None = None
    Slurm: SageMakerClusterOrchestratorSlurmConfig | None = None
