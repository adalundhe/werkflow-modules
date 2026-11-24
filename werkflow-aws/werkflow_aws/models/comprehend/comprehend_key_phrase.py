from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendKeyPhrase(BaseModel):
    Score: StrictFloat | StrictInt | None = None
    Text: StrictStr | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
