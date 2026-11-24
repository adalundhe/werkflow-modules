from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2EbsBlockDevice(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    Iops: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Throughput: StrictInt | None = None
    OutpostArn: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Encrypted: StrictBool | None = None
    VolumeInitializationRate: StrictInt | None = None
    AvailabilityZoneId: StrictStr | None = None
    EbsCardIndex: StrictInt | None = None
