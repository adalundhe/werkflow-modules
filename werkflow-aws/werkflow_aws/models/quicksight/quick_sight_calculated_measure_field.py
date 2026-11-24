from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCalculatedMeasureField(BaseModel):
    FieldId: StrictStr | None = None
    Expression: StrictStr | None = None
