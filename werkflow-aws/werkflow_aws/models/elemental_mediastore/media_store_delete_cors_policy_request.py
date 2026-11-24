from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreDeleteCorsPolicyRequest(BaseModel):
    ContainerName: StrictStr
