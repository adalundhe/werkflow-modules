from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightThousandSeparatorOptions(BaseModel):
    Symbol: StrictStr | None = None
    Visibility: StrictStr | None = None
    GroupingStyle: StrictStr | None = None
