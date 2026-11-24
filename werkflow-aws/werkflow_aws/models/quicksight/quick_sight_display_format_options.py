from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .quick_sight_negative_format import QuickSightNegativeFormat


class QuickSightDisplayFormatOptions(BaseModel):
    UseBlankCellFormat: StrictBool | None = None
    BlankCellFormat: StrictStr | None = None
    DateFormat: StrictStr | None = None
    DecimalSeparator: StrictStr | None = None
    GroupingSeparator: StrictStr | None = None
    UseGrouping: StrictBool | None = None
    FractionDigits: StrictInt | None = None
    Prefix: StrictStr | None = None
    Suffix: StrictStr | None = None
    UnitScaler: StrictStr | None = None
    NegativeFormat: QuickSightNegativeFormat | None = None
    CurrencySymbol: StrictStr | None = None
