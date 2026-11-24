from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_thousand_separator_options import QuickSightThousandSeparatorOptions


class QuickSightNumericSeparatorConfiguration(BaseModel):
    DecimalSeparator: StrictStr | None = None
    ThousandsSeparator: QuickSightThousandSeparatorOptions | None = None
