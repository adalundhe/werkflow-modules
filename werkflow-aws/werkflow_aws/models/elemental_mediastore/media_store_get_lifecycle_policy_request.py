from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreGetLifecyclePolicyRequest(BaseModel):
    ContainerName: StrictStr
