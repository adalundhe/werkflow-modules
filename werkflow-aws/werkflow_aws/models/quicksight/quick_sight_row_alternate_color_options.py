from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRowAlternateColorOptions(BaseModel):
    Status: StrictStr | None = None
    RowAlternateColors: list[StrictStr] | None = None
    UsePrimaryBackgroundColor: StrictStr | None = None
