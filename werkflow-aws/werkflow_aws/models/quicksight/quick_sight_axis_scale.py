from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_linear_scale import QuickSightAxisLinearScale
from .quick_sight_axis_logarithmic_scale import QuickSightAxisLogarithmicScale


class QuickSightAxisScale(BaseModel):
    Linear: QuickSightAxisLinearScale | None = None
    Logarithmic: QuickSightAxisLogarithmicScale | None = None
