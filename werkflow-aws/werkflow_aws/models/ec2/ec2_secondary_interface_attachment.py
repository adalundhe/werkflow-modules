from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2SecondaryInterfaceAttachment(BaseModel):
    AttachmentId: StrictStr | None = None
    AttachTime: datetime.datetime | StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
    DeviceIndex: StrictInt | None = None
    InstanceId: StrictStr | None = None
    InstanceOwnerId: StrictStr | None = None
    NetworkCardIndex: StrictInt | None = None
    Status: StrictStr | None = None
