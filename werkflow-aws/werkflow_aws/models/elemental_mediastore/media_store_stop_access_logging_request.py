from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreStopAccessLoggingRequest(BaseModel):
    ContainerName: StrictStr
