from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_numeric_format_configuration import QuickSightNumericFormatConfiguration


class QuickSightNumberFormatConfiguration(BaseModel):
    FormatConfiguration: QuickSightNumericFormatConfiguration | None = None
