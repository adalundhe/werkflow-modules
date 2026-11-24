from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeoSpatialColumnGroup(BaseModel):
    Name: StrictStr | None = None
    CountryCode: StrictStr | None = None
    Columns: list[StrictStr] | None = None
