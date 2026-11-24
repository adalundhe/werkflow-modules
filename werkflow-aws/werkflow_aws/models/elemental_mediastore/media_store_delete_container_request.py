from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreDeleteContainerRequest(BaseModel):
    ContainerName: StrictStr
