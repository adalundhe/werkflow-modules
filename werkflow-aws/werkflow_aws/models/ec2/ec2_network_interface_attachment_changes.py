from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2NetworkInterfaceAttachmentChanges(BaseModel):
    DefaultEnaQueueCount: StrictBool | None = None
    EnaQueueCount: StrictInt | None = None
    AttachmentId: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
