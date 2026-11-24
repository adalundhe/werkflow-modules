from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSampleValue(BaseModel):
    value: StrictStr | None = None
