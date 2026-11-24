from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_border_settings import QuickSightBorderSettings
from .quick_sight_decal_settings import QuickSightDecalSettings


class QuickSightBarChartDefaultSeriesSettings(BaseModel):
    DecalSettings: QuickSightDecalSettings | None = None
    BorderSettings: QuickSightBorderSettings | None = None
