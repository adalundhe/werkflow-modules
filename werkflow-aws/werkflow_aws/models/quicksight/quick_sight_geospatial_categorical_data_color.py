from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialCategoricalDataColor(BaseModel):
    Color: StrictStr | None = None
    DataValue: StrictStr | None = None
