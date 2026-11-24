from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class QuickSightArcConfiguration(BaseModel):
    ArcAngle: StrictFloat | StrictInt | None = None
    ArcThickness: StrictStr | None = None
