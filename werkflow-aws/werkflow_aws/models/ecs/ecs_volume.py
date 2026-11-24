from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_docker_volume_configuration import ECSDockerVolumeConfiguration
from .ecsefs_volume_configuration import ECSEFSVolumeConfiguration
from .ecsf_sx_windows_file_server_volume_configuration import ECSFSxWindowsFileServerVolumeConfiguration
from .ecs_host_volume_properties import ECSHostVolumeProperties
from .ecss3_files_volume_configuration import ECSS3FilesVolumeConfiguration


class ECSVolume(BaseModel):
    name: StrictStr | None = None
    host: ECSHostVolumeProperties | None = None
    dockerVolumeConfiguration: ECSDockerVolumeConfiguration | None = None
    efsVolumeConfiguration: ECSEFSVolumeConfiguration | None = None
    s3filesVolumeConfiguration: ECSS3FilesVolumeConfiguration | None = None
    fsxWindowsFileServerVolumeConfiguration: ECSFSxWindowsFileServerVolumeConfiguration | None = None
    configuredAtLaunch: StrictBool | None = None
