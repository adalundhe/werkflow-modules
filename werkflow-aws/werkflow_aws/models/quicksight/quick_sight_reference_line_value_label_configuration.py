from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_numeric_format_configuration import QuickSightNumericFormatConfiguration


class QuickSightReferenceLineValueLabelConfiguration(BaseModel):
    RelativePosition: StrictStr | None = None
    FormatConfiguration: QuickSightNumericFormatConfiguration | None = None
