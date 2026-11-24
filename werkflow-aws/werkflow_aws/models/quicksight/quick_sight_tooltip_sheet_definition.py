from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_layout import QuickSightLayout
from .quick_sight_sheet_image import QuickSightSheetImage
from .quick_sight_sheet_text_box import QuickSightSheetTextBox
from .quick_sight_visual import QuickSightVisual


class QuickSightTooltipSheetDefinition(BaseModel):
    SheetId: StrictStr | None = None
    Name: StrictStr | None = None
    Visuals: list[QuickSightVisual] | None = None
    TextBoxes: list[QuickSightSheetTextBox] | None = None
    Images: list[QuickSightSheetImage] | None = None
    Layouts: list[QuickSightLayout] | None = None
