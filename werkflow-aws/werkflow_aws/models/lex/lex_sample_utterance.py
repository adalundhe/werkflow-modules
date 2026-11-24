from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSampleUtterance(BaseModel):
    utterance: StrictStr | None = None
