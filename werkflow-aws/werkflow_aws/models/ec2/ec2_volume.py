from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_attachment import EC2Attachment
from .ec2_operator import EC2Operator
from .ec2_sse_type import EC2SSEType
from .ec2_state import EC2State
from .ec2_tag import EC2Tag
from .ec2_volume_type import EC2VolumeType


class EC2Volume(BaseModel):
    OutpostArn: StrictStr | None = None
    SourceVolumeId: StrictStr | None = None
    Iops: StrictInt | None = None
    Tags: list[EC2Tag] | None = None
    VolumeType: EC2VolumeType | None = None
    FastRestored: StrictBool | None = None
    MultiAttachEnabled: StrictBool | None = None
    Throughput: StrictInt | None = None
    SseType: EC2SSEType | None = None
    Operator: EC2Operator | None = None
    VolumeInitializationRate: StrictInt | None = None
    VolumeArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    VolumeId: StrictStr | None = None
    Size: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    State: EC2State | None = None
    CreateTime: datetime.datetime | None = None
    Attachments: list[EC2Attachment] | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
