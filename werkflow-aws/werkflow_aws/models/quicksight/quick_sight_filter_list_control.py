from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_cascading_control_configuration import QuickSightCascadingControlConfiguration
from .quick_sight_control_sort_configuration import QuickSightControlSortConfiguration
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_filter_selectable_values import QuickSightFilterSelectableValues
from .quick_sight_list_control_display_options import QuickSightListControlDisplayOptions


class QuickSightFilterListControl(BaseModel):
    FilterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceFilterId: StrictStr | None = None
    DisplayOptions: QuickSightListControlDisplayOptions | None = None
    Type: StrictStr | None = None
    SelectableValues: QuickSightFilterSelectableValues | None = None
    CascadingControlConfiguration: QuickSightCascadingControlConfiguration | None = None
    ControlSortConfigurations: list[QuickSightControlSortConfiguration] | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
