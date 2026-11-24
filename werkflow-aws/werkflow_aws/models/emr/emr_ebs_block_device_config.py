from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .emr_volume_specification import EMRVolumeSpecification


class EMREbsBlockDeviceConfig(BaseModel):
    VolumeSpecification: EMRVolumeSpecification
    VolumesPerInstance: StrictInt | None = None
