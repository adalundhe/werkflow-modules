from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_label_options import QuickSightLabelOptions
from .quick_sight_list_control_search_options import QuickSightListControlSearchOptions
from .quick_sight_list_control_select_all_options import QuickSightListControlSelectAllOptions
from .quick_sight_sheet_control_info_icon_label_options import QuickSightSheetControlInfoIconLabelOptions


class QuickSightListControlDisplayOptions(BaseModel):
    SearchOptions: QuickSightListControlSearchOptions | None = None
    SelectAllOptions: QuickSightListControlSelectAllOptions | None = None
    TitleOptions: QuickSightLabelOptions | None = None
    InfoIconLabelOptions: QuickSightSheetControlInfoIconLabelOptions | None = None
