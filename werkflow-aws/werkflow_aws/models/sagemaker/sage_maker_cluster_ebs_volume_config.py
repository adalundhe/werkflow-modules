from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerClusterEbsVolumeConfig(BaseModel):
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    RootVolume: StrictBool | None = None
