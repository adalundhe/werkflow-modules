from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightDataColor(BaseModel):
    Color: StrictStr | None = None
    DataValue: StrictFloat | StrictInt | None = None
