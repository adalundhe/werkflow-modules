from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .quick_sight_arc_axis_display_range import QuickSightArcAxisDisplayRange


class QuickSightArcAxisConfiguration(BaseModel):
    Range: QuickSightArcAxisDisplayRange | None = None
    ReserveRange: StrictInt | None = None
