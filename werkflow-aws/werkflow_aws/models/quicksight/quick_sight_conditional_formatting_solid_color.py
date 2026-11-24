from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightConditionalFormattingSolidColor(BaseModel):
    Expression: StrictStr | None = None
    Color: StrictStr | None = None
