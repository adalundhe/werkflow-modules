from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_sort_configuration import QuickSightControlSortConfiguration
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_hierarchy_filter_drop_down_control_display_options import QuickSightHierarchyFilterDropDownControlDisplayOptions


class QuickSightDefaultHierarchyFilterDropDownControlOptions(BaseModel):
    DisplayOptions: QuickSightHierarchyFilterDropDownControlDisplayOptions | None = None
    Type: StrictStr | None = None
    CommitMode: StrictStr | None = None
    ControlSortConfigurations: list[QuickSightControlSortConfiguration] | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
