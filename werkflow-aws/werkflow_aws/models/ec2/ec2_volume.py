import datetime
from pydantic import (
    BaseModel, 
    StrictStr, 
    StrictInt,
    StrictBool,
)
from typing import Literal
from .ec2_tag import EC2Tag
from .ec2_operator import EC2Operator
from .ec2_attachment import EC2Attachment

EC2VolumeType = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "sc1",
    "st1",
    "gp3",
]

EC2SSEType = Literal[
    "sse-ebs",
    "sse-kms",
    "none",
]

EC2State = Literal[
    "creating",
    "available",
    "in-use",
    "deleting",
    "deleted",
    "error"
]


class EC2Volume(BaseModel):
    OutpostArn: StrictStr | None = None
    Iops: StrictInt
    Tags: list[EC2Tag] | None = None
    VolumeType: EC2VolumeType
    FastRestored: StrictBool
    MultiAttachEnabled: StrictBool
    Throughput: StrictInt
    SseType: EC2SSEType
    Operator: EC2Operator | None = None
    VolumeInitializationRate: StrictInt
    VolumeId: StrictStr
    Size: StrictInt
    SnapshotId: StrictStr
    AvailabilityZone: StrictStr
    State: EC2State
    CreateTime: datetime.datetime
    Attachments: list[EC2Attachment] | None = None
    Encrypted: StrictBool = False
    KmsKeyId: StrictStr | None = None

