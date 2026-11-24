from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_grid_layout_element_background_style import QuickSightGridLayoutElementBackgroundStyle
from .quick_sight_grid_layout_element_border_style import QuickSightGridLayoutElementBorderStyle
from .quick_sight_loading_animation import QuickSightLoadingAnimation


class QuickSightGridLayoutElement(BaseModel):
    ElementId: StrictStr | None = None
    ElementType: StrictStr | None = None
    ColumnIndex: StrictInt | None = None
    ColumnSpan: StrictInt | None = None
    RowIndex: StrictInt | None = None
    RowSpan: StrictInt | None = None
    BorderStyle: QuickSightGridLayoutElementBorderStyle | None = None
    SelectedBorderStyle: QuickSightGridLayoutElementBorderStyle | None = None
    BackgroundStyle: QuickSightGridLayoutElementBackgroundStyle | None = None
    LoadingAnimation: QuickSightLoadingAnimation | None = None
    BorderRadius: StrictStr | None = None
    Padding: StrictStr | None = None
