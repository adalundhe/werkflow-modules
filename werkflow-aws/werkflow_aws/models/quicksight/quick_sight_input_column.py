from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightInputColumn(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    SubType: StrictStr | None = None
