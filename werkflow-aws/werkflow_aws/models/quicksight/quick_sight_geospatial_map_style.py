from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialMapStyle(BaseModel):
    BaseMapStyle: StrictStr | None = None
    BackgroundColor: StrictStr | None = None
    BaseMapVisibility: StrictStr | None = None
