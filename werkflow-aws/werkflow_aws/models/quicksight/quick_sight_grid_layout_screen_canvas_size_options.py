from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGridLayoutScreenCanvasSizeOptions(BaseModel):
    ResizeOption: StrictStr | None = None
    OptimizedViewPortWidth: StrictStr | None = None
