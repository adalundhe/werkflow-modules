from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSimpleClusterMarker(BaseModel):
    Color: StrictStr | None = None
