from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_axis_label_reference_options import QuickSightAxisLabelReferenceOptions
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightAxisLabelOptions(BaseModel):
    FontConfiguration: QuickSightFontConfiguration | None = None
    CustomLabel: StrictStr | None = None
    ApplyTo: QuickSightAxisLabelReferenceOptions | None = None
