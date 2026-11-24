from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2EbsBlockDeviceResponse(BaseModel):
    Encrypted: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Iops: StrictInt | None = None
    Throughput: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
