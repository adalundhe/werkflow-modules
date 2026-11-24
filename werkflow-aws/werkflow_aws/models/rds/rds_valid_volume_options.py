from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_valid_storage_options import RDSValidStorageOptions


class RDSValidVolumeOptions(BaseModel):
    VolumeName: StrictStr | None = None
    Storage: list[RDSValidStorageOptions] | None = None
