from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_cluster_ebs_volume_config import SageMakerClusterEbsVolumeConfig
from .sage_maker_cluster_fsx_lustre_config import SageMakerClusterFsxLustreConfig
from .sage_maker_cluster_fsx_open_zfs_config import SageMakerClusterFsxOpenZfsConfig


class SageMakerClusterInstanceStorageConfig(BaseModel):
    EbsVolumeConfig: SageMakerClusterEbsVolumeConfig | None = None
    FsxLustreConfig: SageMakerClusterFsxLustreConfig | None = None
    FsxOpenZfsConfig: SageMakerClusterFsxOpenZfsConfig | None = None
