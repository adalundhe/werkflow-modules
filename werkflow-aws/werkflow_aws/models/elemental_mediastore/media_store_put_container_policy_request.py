from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStorePutContainerPolicyRequest(BaseModel):
    ContainerName: StrictStr
    Policy: StrictStr
