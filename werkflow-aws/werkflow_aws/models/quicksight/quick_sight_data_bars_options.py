from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataBarsOptions(BaseModel):
    FieldId: StrictStr | None = None
    PositiveColor: StrictStr | None = None
    NegativeColor: StrictStr | None = None
