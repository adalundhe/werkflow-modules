from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStorePutLifecyclePolicyRequest(BaseModel):
    ContainerName: StrictStr
    LifecyclePolicy: StrictStr
