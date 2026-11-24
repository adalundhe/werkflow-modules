from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_cascading_control_configuration import QuickSightCascadingControlConfiguration
from .quick_sight_control_sort_configuration import QuickSightControlSortConfiguration
from .quick_sight_control_title_format_text import QuickSightControlTitleFormatText
from .quick_sight_list_control_display_options import QuickSightListControlDisplayOptions
from .quick_sight_parameter_selectable_values import QuickSightParameterSelectableValues


class QuickSightParameterListControl(BaseModel):
    ParameterControlId: StrictStr | None = None
    Title: StrictStr | None = None
    SourceParameterName: StrictStr | None = None
    DisplayOptions: QuickSightListControlDisplayOptions | None = None
    Type: StrictStr | None = None
    SelectableValues: QuickSightParameterSelectableValues | None = None
    CascadingControlConfiguration: QuickSightCascadingControlConfiguration | None = None
    ControlSortConfigurations: list[QuickSightControlSortConfiguration] | None = None
    ControlTitleFormatText: QuickSightControlTitleFormatText | None = None
