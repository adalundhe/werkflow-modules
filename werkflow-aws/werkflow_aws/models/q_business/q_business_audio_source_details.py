from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessAudioSourceDetails(BaseModel):
    mediaId: StrictStr | None = None
    mediaMimeType: StrictStr | None = None
    startTimeMilliseconds: StrictInt | None = None
    endTimeMilliseconds: StrictInt | None = None
    audioExtractionType: StrictStr | None = None
