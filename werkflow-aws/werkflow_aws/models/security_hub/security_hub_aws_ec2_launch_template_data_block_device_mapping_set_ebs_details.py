from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    Encrypted: StrictBool | None = None
    Iops: StrictInt | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Throughput: StrictInt | None = None
    VolumeSize: StrictInt | None = None
    VolumeType: StrictStr | None = None
