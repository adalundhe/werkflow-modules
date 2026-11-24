from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_label_options import QuickSightLabelOptions
from .quick_sight_sheet_control_info_icon_label_options import QuickSightSheetControlInfoIconLabelOptions


class QuickSightSliderControlDisplayOptions(BaseModel):
    TitleOptions: QuickSightLabelOptions | None = None
    InfoIconLabelOptions: QuickSightSheetControlInfoIconLabelOptions | None = None
