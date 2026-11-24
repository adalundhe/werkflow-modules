from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamCopyImageRequest(BaseModel):
    SourceImageName: StrictStr
    DestinationImageName: StrictStr
    DestinationRegion: StrictStr
    DestinationImageDescription: StrictStr | None = None
