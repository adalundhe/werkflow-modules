from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_label_options import QuickSightLabelOptions
from .quick_sight_sheet_control_info_icon_label_options import QuickSightSheetControlInfoIconLabelOptions
from .quick_sight_text_control_placeholder_options import QuickSightTextControlPlaceholderOptions


class QuickSightTextFieldControlDisplayOptions(BaseModel):
    TitleOptions: QuickSightLabelOptions | None = None
    PlaceholderOptions: QuickSightTextControlPlaceholderOptions | None = None
    InfoIconLabelOptions: QuickSightSheetControlInfoIconLabelOptions | None = None
