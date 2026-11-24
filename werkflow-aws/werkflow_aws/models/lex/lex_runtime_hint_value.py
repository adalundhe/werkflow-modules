from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexRuntimeHintValue(BaseModel):
    phrase: StrictStr | None = None
