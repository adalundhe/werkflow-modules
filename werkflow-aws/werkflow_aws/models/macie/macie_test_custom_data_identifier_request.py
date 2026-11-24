from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieTestCustomDataIdentifierRequest(BaseModel):
    regex: StrictStr
    sampleText: StrictStr
    ignoreWords: list[StrictStr] | None = None
    keywords: list[StrictStr] | None = None
    maximumMatchDistance: StrictInt | None = None
