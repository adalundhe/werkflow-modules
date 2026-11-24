from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .rds_valid_volume_options import RDSValidVolumeOptions


class RDSValidAdditionalStorageOptions(BaseModel):
    SupportsAdditionalStorageVolumes: StrictBool | None = None
    Volumes: list[RDSValidVolumeOptions] | None = None
