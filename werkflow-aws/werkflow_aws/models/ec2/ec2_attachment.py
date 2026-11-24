import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from typing import Literal


EC2AttachmentState = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "busy",
]


class EC2Attachment(BaseModel):
    DeleteOnTermination: StrictBool | None = None
    AssociatedResource: StrictStr | None = None
    InstanceOwningService: StrictStr | None = None
    VolumeId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Device: StrictStr | None = None
    State: EC2AttachmentState | None = None
    AttachTime: datetime.datetime | None = None
