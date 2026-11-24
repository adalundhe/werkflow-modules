from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnSchema(BaseModel):
    Name: StrictStr | None = None
    DataType: StrictStr | None = None
    GeographicRole: StrictStr | None = None
