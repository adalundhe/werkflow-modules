from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_free_form_layout_element_background_style import QuickSightFreeFormLayoutElementBackgroundStyle
from .quick_sight_free_form_layout_element_border_style import QuickSightFreeFormLayoutElementBorderStyle
from .quick_sight_loading_animation import QuickSightLoadingAnimation
from .quick_sight_sheet_element_rendering_rule import QuickSightSheetElementRenderingRule


class QuickSightFreeFormLayoutElement(BaseModel):
    ElementId: StrictStr | None = None
    ElementType: StrictStr | None = None
    XAxisLocation: StrictStr | None = None
    YAxisLocation: StrictStr | None = None
    Width: StrictStr | None = None
    Height: StrictStr | None = None
    Visibility: StrictStr | None = None
    RenderingRules: list[QuickSightSheetElementRenderingRule] | None = None
    BorderStyle: QuickSightFreeFormLayoutElementBorderStyle | None = None
    SelectedBorderStyle: QuickSightFreeFormLayoutElementBorderStyle | None = None
    BackgroundStyle: QuickSightFreeFormLayoutElementBackgroundStyle | None = None
    LoadingAnimation: QuickSightLoadingAnimation | None = None
    BorderRadius: StrictStr | None = None
    Padding: StrictStr | None = None
