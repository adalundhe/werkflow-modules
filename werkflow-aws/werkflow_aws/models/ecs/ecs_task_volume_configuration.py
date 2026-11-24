from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_task_managed_ebs_volume_configuration import ECSTaskManagedEBSVolumeConfiguration


class ECSTaskVolumeConfiguration(BaseModel):
    name: StrictStr
    managedEBSVolume: ECSTaskManagedEBSVolumeConfiguration | None = None
