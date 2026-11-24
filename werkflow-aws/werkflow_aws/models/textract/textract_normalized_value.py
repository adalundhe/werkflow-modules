from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractNormalizedValue(BaseModel):
    Value: StrictStr | None = None
    ValueType: StrictStr | None = None
