from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_parameter_date_time_picker_control import QuickSightParameterDateTimePickerControl
from .quick_sight_parameter_drop_down_control import QuickSightParameterDropDownControl
from .quick_sight_parameter_list_control import QuickSightParameterListControl
from .quick_sight_parameter_slider_control import QuickSightParameterSliderControl
from .quick_sight_parameter_text_area_control import QuickSightParameterTextAreaControl
from .quick_sight_parameter_text_field_control import QuickSightParameterTextFieldControl


class QuickSightParameterControl(BaseModel):
    DateTimePicker: QuickSightParameterDateTimePickerControl | None = None
    List: QuickSightParameterListControl | None = None
    Dropdown: QuickSightParameterDropDownControl | None = None
    TextField: QuickSightParameterTextFieldControl | None = None
    TextArea: QuickSightParameterTextAreaControl | None = None
    Slider: QuickSightParameterSliderControl | None = None
