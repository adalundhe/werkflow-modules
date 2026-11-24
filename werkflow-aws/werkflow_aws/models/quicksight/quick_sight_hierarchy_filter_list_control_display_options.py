from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_hierarchy_filter_list_control_search_options import QuickSightHierarchyFilterListControlSearchOptions
from .quick_sight_label_options import QuickSightLabelOptions
from .quick_sight_sheet_control_info_icon_label_options import QuickSightSheetControlInfoIconLabelOptions


class QuickSightHierarchyFilterListControlDisplayOptions(BaseModel):
    TitleOptions: QuickSightLabelOptions | None = None
    InfoIconLabelOptions: QuickSightSheetControlInfoIconLabelOptions | None = None
    SearchOptions: QuickSightHierarchyFilterListControlSearchOptions | None = None
