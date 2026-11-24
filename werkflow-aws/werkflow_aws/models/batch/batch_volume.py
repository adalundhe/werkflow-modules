from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .batch_efs_volume_configuration import BatchEFSVolumeConfiguration
from .batch_host import BatchHost
from .batch_s3_files_volume_configuration import BatchS3FilesVolumeConfiguration


class BatchVolume(BaseModel):
    host: BatchHost | None = None
    name: StrictStr | None = None
    efsVolumeConfiguration: BatchEFSVolumeConfiguration | None = None
    s3filesVolumeConfiguration: BatchS3FilesVolumeConfiguration | None = None
