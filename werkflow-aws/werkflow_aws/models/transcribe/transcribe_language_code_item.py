from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class TranscribeLanguageCodeItem(BaseModel):
    LanguageCode: StrictStr | None = None
    DurationInSeconds: StrictFloat | StrictInt | None = None
