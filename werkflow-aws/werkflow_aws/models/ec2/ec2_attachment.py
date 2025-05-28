import datetime
from pydantic import BaseModel, StrictStr, StrictBool
from typing import Literal


EC2AttachmentState = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "busy",
]

class EC2Attachment(BaseModel):
    DeleteOnTermination: StrictBool = False
    AssociatedResource: StrictStr
    InstanceOwningService: StrictStr
    VolumeId: StrictStr
    InstanceId: StrictStr
    Device: StrictStr
    State: EC2AttachmentState
    AttachTime: datetime.datetime