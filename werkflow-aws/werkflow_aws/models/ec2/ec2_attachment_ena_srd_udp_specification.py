from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2AttachmentEnaSrdUdpSpecification(BaseModel):
    EnaSrdUdpEnabled: StrictBool | None = None
