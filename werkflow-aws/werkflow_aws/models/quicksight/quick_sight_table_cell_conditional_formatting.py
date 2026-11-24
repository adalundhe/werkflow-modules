from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_text_conditional_format import QuickSightTextConditionalFormat


class QuickSightTableCellConditionalFormatting(BaseModel):
    FieldId: StrictStr | None = None
    TextFormat: QuickSightTextConditionalFormat | None = None
