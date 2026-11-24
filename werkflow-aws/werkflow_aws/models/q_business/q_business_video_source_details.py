from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessVideoSourceDetails(BaseModel):
    mediaId: StrictStr | None = None
    mediaMimeType: StrictStr | None = None
    startTimeMilliseconds: StrictInt | None = None
    endTimeMilliseconds: StrictInt | None = None
    videoExtractionType: StrictStr | None = None
