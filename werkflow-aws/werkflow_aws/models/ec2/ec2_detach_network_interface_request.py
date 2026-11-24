from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DetachNetworkInterfaceRequest(BaseModel):
    AttachmentId: StrictStr
    DryRun: StrictBool | None = None
    Force: StrictBool | None = None
