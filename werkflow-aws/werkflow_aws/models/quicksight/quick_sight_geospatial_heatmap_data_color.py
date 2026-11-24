from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeospatialHeatmapDataColor(BaseModel):
    Color: StrictStr | None = None
