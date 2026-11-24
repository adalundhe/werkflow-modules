from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2FleetEbsBlockDeviceRequest(BaseModel):
    Encrypted: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Iops: StrictInt | None = None
    Throughput: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: Literal['standard', 'io1', 'io2', 'gp2', 'sc1', 'st1', 'gp3'] | None = None
