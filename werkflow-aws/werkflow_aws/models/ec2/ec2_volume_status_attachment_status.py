from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VolumeStatusAttachmentStatus(BaseModel):
    IoPerformance: StrictStr | None = None
    InstanceId: StrictStr | None = None
