from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldLastUsed(BaseModel):
    type: StrictStr | None = None
    value: StrictStr | None = None
