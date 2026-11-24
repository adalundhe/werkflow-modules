from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_slider_control_display_options import QuickSightSliderControlDisplayOptions


class QuickSightDefaultSliderControlOptions(BaseModel):
    DisplayOptions: QuickSightSliderControlDisplayOptions | None = None
    Type: StrictStr | None = None
    MaximumValue: StrictFloat | StrictInt | None = None
    MinimumValue: StrictFloat | StrictInt | None = None
    StepSize: StrictFloat | StrictInt | None = None
