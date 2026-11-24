from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialMapStyleOptions(BaseModel):
    BaseMapStyle: StrictStr | None = None
