from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PollyPutLexiconRequest(BaseModel):
    Name: StrictStr
    Content: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
