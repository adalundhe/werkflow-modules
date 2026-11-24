from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_control_sort_configuration import QuickSightControlSortConfiguration
from .quick_sight_drop_down_control_display_options import QuickSightDropDownControlDisplayOptions
from .quick_sight_filter_selectable_values import QuickSightFilterSelectableValues


class QuickSightDefaultFilterDropDownControlOptions(BaseModel):
    DisplayOptions: QuickSightDropDownControlDisplayOptions | None = None
    Type: StrictStr | None = None
    SelectableValues: QuickSightFilterSelectableValues | None = None
    CommitMode: StrictStr | None = None
    ControlSortConfigurations: list[QuickSightControlSortConfiguration] | None = None
