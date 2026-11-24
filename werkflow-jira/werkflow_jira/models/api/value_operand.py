from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ValueOperand(BaseModel):
    encodedValue: StrictStr | None = None
    value: StrictStr | None = None
