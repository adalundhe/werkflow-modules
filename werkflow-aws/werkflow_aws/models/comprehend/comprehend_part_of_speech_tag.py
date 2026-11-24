from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendPartOfSpeechTag(BaseModel):
    Tag: StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
