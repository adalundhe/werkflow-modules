from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieSeverity(BaseModel):
    description: StrictStr | None = None
    score: StrictInt | None = None
