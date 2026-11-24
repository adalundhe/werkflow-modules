from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightConditionalFormattingCustomIconOptions(BaseModel):
    Icon: StrictStr | None = None
    UnicodeIcon: StrictStr | None = None
