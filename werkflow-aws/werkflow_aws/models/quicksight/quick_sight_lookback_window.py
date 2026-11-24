from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightLookbackWindow(BaseModel):
    ColumnName: StrictStr | None = None
    Size: StrictInt | None = None
    SizeUnit: StrictStr | None = None
