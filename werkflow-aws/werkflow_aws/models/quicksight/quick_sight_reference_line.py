from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_reference_line_data_configuration import QuickSightReferenceLineDataConfiguration
from .quick_sight_reference_line_label_configuration import QuickSightReferenceLineLabelConfiguration
from .quick_sight_reference_line_style_configuration import QuickSightReferenceLineStyleConfiguration


class QuickSightReferenceLine(BaseModel):
    Status: StrictStr | None = None
    DataConfiguration: QuickSightReferenceLineDataConfiguration | None = None
    StyleConfiguration: QuickSightReferenceLineStyleConfiguration | None = None
    LabelConfiguration: QuickSightReferenceLineLabelConfiguration | None = None
