from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AutoScalingEbs(BaseModel):
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    Iops: StrictInt | None = None
    Encrypted: StrictBool | None = None
    Throughput: StrictInt | None = None
