from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_host_volume_properties import ECSHostVolumeProperties
from .ecs_log_driver_volume_configuration import ECSLogDriverVolumeConfiguration


class ECSDaemonVolume(BaseModel):
    name: StrictStr | None = None
    host: ECSHostVolumeProperties | None = None
    logDriverVolumeConfiguration: ECSLogDriverVolumeConfiguration | None = None
