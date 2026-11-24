from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_line_chart_series_settings import QuickSightLineChartSeriesSettings


class QuickSightDataFieldSeriesItem(BaseModel):
    FieldId: StrictStr | None = None
    FieldValue: StrictStr | None = None
    AxisBinding: StrictStr | None = None
    Settings: QuickSightLineChartSeriesSettings | None = None
