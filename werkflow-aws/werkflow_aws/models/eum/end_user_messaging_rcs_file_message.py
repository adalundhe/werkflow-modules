from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsFileMessage(BaseModel):
    FileUrl: StrictStr
    ThumbnailUrl: StrictStr | None = None
