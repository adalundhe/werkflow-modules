from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightConditionalFormattingIconDisplayConfiguration(BaseModel):
    IconDisplayOption: StrictStr | None = None
