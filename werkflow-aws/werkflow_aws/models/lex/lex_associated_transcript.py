from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexAssociatedTranscript(BaseModel):
    transcript: StrictStr | None = None
