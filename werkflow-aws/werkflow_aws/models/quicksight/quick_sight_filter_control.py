from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_filter_cross_sheet_control import QuickSightFilterCrossSheetControl
from .quick_sight_filter_date_time_picker_control import QuickSightFilterDateTimePickerControl
from .quick_sight_filter_drop_down_control import QuickSightFilterDropDownControl
from .quick_sight_filter_list_control import QuickSightFilterListControl
from .quick_sight_filter_relative_date_time_control import QuickSightFilterRelativeDateTimeControl
from .quick_sight_filter_slider_control import QuickSightFilterSliderControl
from .quick_sight_filter_text_area_control import QuickSightFilterTextAreaControl
from .quick_sight_filter_text_field_control import QuickSightFilterTextFieldControl
from .quick_sight_hierarchy_filter_drop_down_control import QuickSightHierarchyFilterDropDownControl
from .quick_sight_hierarchy_filter_list_control import QuickSightHierarchyFilterListControl


class QuickSightFilterControl(BaseModel):
    DateTimePicker: QuickSightFilterDateTimePickerControl | None = None
    List: QuickSightFilterListControl | None = None
    Dropdown: QuickSightFilterDropDownControl | None = None
    TextField: QuickSightFilterTextFieldControl | None = None
    TextArea: QuickSightFilterTextAreaControl | None = None
    Slider: QuickSightFilterSliderControl | None = None
    RelativeDateTime: QuickSightFilterRelativeDateTimeControl | None = None
    CrossSheet: QuickSightFilterCrossSheetControl | None = None
    HierarchyList: QuickSightHierarchyFilterListControl | None = None
    HierarchyDropdown: QuickSightHierarchyFilterDropDownControl | None = None
