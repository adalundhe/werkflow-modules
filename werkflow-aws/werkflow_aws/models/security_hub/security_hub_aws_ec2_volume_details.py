from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ec2_volume_attachment import SecurityHubAwsEc2VolumeAttachment


class SecurityHubAwsEc2VolumeDetails(BaseModel):
    CreateTime: StrictStr | None = None
    DeviceName: StrictStr | None = None
    Encrypted: StrictBool | None = None
    Size: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    Status: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Attachments: list[SecurityHubAwsEc2VolumeAttachment] | None = None
    VolumeId: StrictStr | None = None
    VolumeType: StrictStr | None = None
    VolumeScanStatus: StrictStr | None = None
