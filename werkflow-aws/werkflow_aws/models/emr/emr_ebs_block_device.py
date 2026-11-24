from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_volume_specification import EMRVolumeSpecification


class EMREbsBlockDevice(BaseModel):
    VolumeSpecification: EMRVolumeSpecification | None = None
    Device: StrictStr | None = None
