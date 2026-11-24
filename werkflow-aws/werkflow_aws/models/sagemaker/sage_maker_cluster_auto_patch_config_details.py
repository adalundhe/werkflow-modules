from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_cluster_drain_policy import SageMakerClusterDrainPolicy
from .sage_maker_cluster_patch_schedule_details import SageMakerClusterPatchScheduleDetails
from .sage_maker_deployment_configuration import SageMakerDeploymentConfiguration


class SageMakerClusterAutoPatchConfigDetails(BaseModel):
    PatchingStrategy: StrictStr | None = None
    CurrentPatchSchedule: SageMakerClusterPatchScheduleDetails | None = None
    DesiredPatchSchedule: SageMakerClusterPatchScheduleDetails | None = None
    DeploymentConfig: SageMakerDeploymentConfiguration | None = None
    IdleWaitWindowInSeconds: StrictInt | None = None
    DrainPolicy: SageMakerClusterDrainPolicy | None = None
