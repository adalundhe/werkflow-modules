from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightGeospatialLineWidth(BaseModel):
    LineWidth: StrictFloat | StrictInt | None = None
