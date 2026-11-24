from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomColor(BaseModel):
    FieldValue: StrictStr | None = None
    Color: StrictStr | None = None
    SpecialValue: StrictStr | None = None
