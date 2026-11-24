from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreDeleteContainerPolicyRequest(BaseModel):
    ContainerName: StrictStr
