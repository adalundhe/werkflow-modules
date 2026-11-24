from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse
from .ec2_tag_model import EC2TagModel
from .ec2_volume_attachment import EC2VolumeAttachment


class EC2VolumeModel(BaseModel):
    AvailabilityZoneId: StrictStr | None = None
    OutpostArn: StrictStr | None = None
    SourceVolumeId: StrictStr | None = None
    Iops: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
    VolumeType: StrictStr | None = None
    FastRestored: StrictBool | None = None
    MultiAttachEnabled: StrictBool | None = None
    Throughput: StrictInt | None = None
    SseType: StrictStr | None = None
    Operator: EC2OperatorResponse | None = None
    VolumeInitializationRate: StrictInt | None = None
    VolumeArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    VolumeId: StrictStr | None = None
    Size: StrictInt | None = None
    SnapshotId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    State: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Attachments: list[EC2VolumeAttachment] | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
