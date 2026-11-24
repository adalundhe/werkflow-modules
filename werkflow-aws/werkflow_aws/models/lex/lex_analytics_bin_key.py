from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexAnalyticsBinKey(BaseModel):
    name: StrictStr | None = None
    value: StrictInt | None = None
