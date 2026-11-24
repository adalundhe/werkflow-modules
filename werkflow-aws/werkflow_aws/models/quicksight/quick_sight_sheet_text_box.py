from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_text_box_interaction_options import QuickSightTextBoxInteractionOptions


class QuickSightSheetTextBox(BaseModel):
    SheetTextBoxId: StrictStr | None = None
    Content: StrictStr | None = None
    Interactions: QuickSightTextBoxInteractionOptions | None = None
