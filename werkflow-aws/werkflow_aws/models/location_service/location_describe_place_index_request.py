from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribePlaceIndexRequest(BaseModel):
    IndexName: StrictStr
