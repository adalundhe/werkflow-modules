from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_service_managed_ebs_volume_configuration import ECSServiceManagedEBSVolumeConfiguration


class ECSServiceVolumeConfiguration(BaseModel):
    name: StrictStr | None = None
    managedEBSVolume: ECSServiceManagedEBSVolumeConfiguration | None = None
