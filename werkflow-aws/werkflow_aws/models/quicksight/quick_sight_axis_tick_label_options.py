from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .quick_sight_label_options import QuickSightLabelOptions


class QuickSightAxisTickLabelOptions(BaseModel):
    LabelOptions: QuickSightLabelOptions | None = None
    RotationAngle: StrictFloat | StrictInt | None = None
