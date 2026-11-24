from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_bar_chart_series_settings import QuickSightBarChartSeriesSettings


class QuickSightDataFieldBarSeriesItem(BaseModel):
    FieldId: StrictStr | None = None
    FieldValue: StrictStr | None = None
    Settings: QuickSightBarChartSeriesSettings | None = None
