from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ScheduledInstancesEbs(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    Encrypted: StrictBool | None = None
    Iops: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
