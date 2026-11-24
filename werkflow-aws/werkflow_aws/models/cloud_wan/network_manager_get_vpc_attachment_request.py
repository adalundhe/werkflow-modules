from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerGetVpcAttachmentRequest(BaseModel):
    AttachmentId: StrictStr
