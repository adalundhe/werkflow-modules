from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightGeospatialNullSymbolStyle(BaseModel):
    FillColor: StrictStr | None = None
    StrokeColor: StrictStr | None = None
    StrokeWidth: StrictFloat | StrictInt | None = None
