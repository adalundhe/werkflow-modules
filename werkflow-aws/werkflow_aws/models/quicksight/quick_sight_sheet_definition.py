from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_filter_control import QuickSightFilterControl
from .quick_sight_layout import QuickSightLayout
from .quick_sight_parameter_control import QuickSightParameterControl
from .quick_sight_sheet_control_layout import QuickSightSheetControlLayout
from .quick_sight_sheet_image import QuickSightSheetImage
from .quick_sight_sheet_text_box import QuickSightSheetTextBox
from .quick_sight_visual import QuickSightVisual
from .quick_sight_visual_custom_action_defaults import QuickSightVisualCustomActionDefaults


class QuickSightSheetDefinition(BaseModel):
    SheetId: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    ParameterControls: list[QuickSightParameterControl] | None = None
    FilterControls: list[QuickSightFilterControl] | None = None
    Visuals: list[QuickSightVisual] | None = None
    TextBoxes: list[QuickSightSheetTextBox] | None = None
    Images: list[QuickSightSheetImage] | None = None
    Layouts: list[QuickSightLayout] | None = None
    SheetControlLayouts: list[QuickSightSheetControlLayout] | None = None
    ContentType: StrictStr | None = None
    CustomActionDefaults: QuickSightVisualCustomActionDefaults | None = None
