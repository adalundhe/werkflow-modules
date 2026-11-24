from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_sort_configuration import QuickSightControlSortConfiguration
from .quick_sight_filter_selectable_values import QuickSightFilterSelectableValues
from .quick_sight_list_control_display_options import QuickSightListControlDisplayOptions


class QuickSightDefaultFilterListControlOptions(BaseModel):
    DisplayOptions: QuickSightListControlDisplayOptions | None = None
    Type: StrictStr | None = None
    SelectableValues: QuickSightFilterSelectableValues | None = None
    ControlSortConfigurations: list[QuickSightControlSortConfiguration] | None = None
