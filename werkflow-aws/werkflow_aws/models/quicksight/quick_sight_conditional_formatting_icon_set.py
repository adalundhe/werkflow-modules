from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightConditionalFormattingIconSet(BaseModel):
    Expression: StrictStr | None = None
    IconSetType: StrictStr | None = None
