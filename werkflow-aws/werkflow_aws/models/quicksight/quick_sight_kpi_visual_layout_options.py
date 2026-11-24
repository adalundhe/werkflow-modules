from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_kpi_visual_standard_layout import QuickSightKPIVisualStandardLayout


class QuickSightKPIVisualLayoutOptions(BaseModel):
    StandardLayout: QuickSightKPIVisualStandardLayout | None = None
