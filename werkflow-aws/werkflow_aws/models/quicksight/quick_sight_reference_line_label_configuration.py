from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration
from .quick_sight_reference_line_custom_label_configuration import QuickSightReferenceLineCustomLabelConfiguration
from .quick_sight_reference_line_value_label_configuration import QuickSightReferenceLineValueLabelConfiguration


class QuickSightReferenceLineLabelConfiguration(BaseModel):
    ValueLabelConfiguration: QuickSightReferenceLineValueLabelConfiguration | None = None
    CustomLabelConfiguration: QuickSightReferenceLineCustomLabelConfiguration | None = None
    FontConfiguration: QuickSightFontConfiguration | None = None
    FontColor: StrictStr | None = None
    HorizontalPosition: StrictStr | None = None
    VerticalPosition: StrictStr | None = None
