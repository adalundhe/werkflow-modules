from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFreeFormLayoutScreenCanvasSizeOptions(BaseModel):
    OptimizedViewPortWidth: StrictStr | None = None
