from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsCarouselCardMedia(BaseModel):
    FileUrl: StrictStr
    ThumbnailUrl: StrictStr | None = None
    Height: StrictStr | None = None
