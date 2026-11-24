from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeocoderHierarchy(BaseModel):
    Country: StrictStr | None = None
    State: StrictStr | None = None
    County: StrictStr | None = None
    City: StrictStr | None = None
    PostCode: StrictStr | None = None
