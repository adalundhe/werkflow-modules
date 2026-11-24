from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .sage_maker_cluster_drain_policy import SageMakerClusterDrainPolicy
from .sage_maker_cluster_patch_schedule import SageMakerClusterPatchSchedule
from .sage_maker_deployment_configuration import SageMakerDeploymentConfiguration


class SageMakerClusterAutoPatchConfig(BaseModel):
    PatchingStrategy: Literal['WhenIdle', 'WhenAllIdle', 'DrainFirst']
    PatchSchedule: SageMakerClusterPatchSchedule | None = None
    DeploymentConfig: SageMakerDeploymentConfiguration | None = None
    IdleWaitWindowInSeconds: StrictInt | None = None
    DrainPolicy: SageMakerClusterDrainPolicy | None = None
