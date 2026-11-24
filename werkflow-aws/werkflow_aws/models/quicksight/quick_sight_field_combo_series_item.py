from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_combo_chart_series_settings import QuickSightComboChartSeriesSettings


class QuickSightFieldComboSeriesItem(BaseModel):
    FieldId: StrictStr | None = None
    Settings: QuickSightComboChartSeriesSettings | None = None
