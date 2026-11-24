from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDeleteArchiveRequest(BaseModel):
    ArchiveName: StrictStr
