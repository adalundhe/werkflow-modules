from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2LaunchTemplateEbsBlockDevice(BaseModel):
    Encrypted: StrictBool | None = None
    DeleteOnTermination: StrictBool | None = None
    Iops: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
    Throughput: StrictInt | None = None
    VolumeInitializationRate: StrictInt | None = None
    EbsCardIndex: StrictInt | None = None
