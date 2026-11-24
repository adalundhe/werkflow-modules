from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreStartAccessLoggingRequest(BaseModel):
    ContainerName: StrictStr
