from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSlotDefaultValue(BaseModel):
    defaultValue: StrictStr | None = None
