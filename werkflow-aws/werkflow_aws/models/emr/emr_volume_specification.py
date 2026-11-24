from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRVolumeSpecification(BaseModel):
    VolumeType: StrictStr | None = None
    Iops: StrictInt | None = None
    SizeInGB: StrictInt | None = None
    Throughput: StrictInt | None = None
