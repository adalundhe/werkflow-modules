from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration
from .quick_sight_label_options import QuickSightLabelOptions


class QuickSightLegendOptions(BaseModel):
    Visibility: StrictStr | None = None
    Title: QuickSightLabelOptions | None = None
    Position: StrictStr | None = None
    Width: StrictStr | None = None
    Height: StrictStr | None = None
    ValueFontConfiguration: QuickSightFontConfiguration | None = None
