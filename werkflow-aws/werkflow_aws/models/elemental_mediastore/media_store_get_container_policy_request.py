from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreGetContainerPolicyRequest(BaseModel):
    ContainerName: StrictStr
