from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_arc_options import QuickSightArcOptions
from .quick_sight_donut_center_options import QuickSightDonutCenterOptions


class QuickSightDonutOptions(BaseModel):
    ArcOptions: QuickSightArcOptions | None = None
    DonutCenterOptions: QuickSightDonutCenterOptions | None = None
