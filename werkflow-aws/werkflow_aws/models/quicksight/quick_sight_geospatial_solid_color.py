from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialSolidColor(BaseModel):
    Color: StrictStr | None = None
    State: StrictStr | None = None
