from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightOutputColumn(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    SubType: StrictStr | None = None
