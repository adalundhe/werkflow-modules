from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeMedia(BaseModel):
    MediaFileUri: StrictStr | None = None
    RedactedMediaFileUri: StrictStr | None = None
