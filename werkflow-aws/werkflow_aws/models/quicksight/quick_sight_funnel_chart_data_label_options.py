from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightFunnelChartDataLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    CategoryLabelVisibility: StrictStr | None = None
    MeasureLabelVisibility: StrictStr | None = None
    Position: StrictStr | None = None
    LabelFontConfiguration: QuickSightFontConfiguration | None = None
    LabelColor: StrictStr | None = None
    MeasureDataLabelStyle: StrictStr | None = None
