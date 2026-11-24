from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_panel_title_options import QuickSightPanelTitleOptions


class QuickSightPanelConfiguration(BaseModel):
    Title: QuickSightPanelTitleOptions | None = None
    BorderVisibility: StrictStr | None = None
    BorderThickness: StrictStr | None = None
    BorderStyle: StrictStr | None = None
    BorderColor: StrictStr | None = None
    GutterVisibility: StrictStr | None = None
    GutterSpacing: StrictStr | None = None
    BackgroundVisibility: StrictStr | None = None
    BackgroundColor: StrictStr | None = None
