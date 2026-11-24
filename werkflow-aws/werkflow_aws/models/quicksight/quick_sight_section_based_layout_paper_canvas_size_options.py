from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_spacing import QuickSightSpacing


class QuickSightSectionBasedLayoutPaperCanvasSizeOptions(BaseModel):
    PaperSize: StrictStr | None = None
    PaperOrientation: StrictStr | None = None
    PaperMargin: QuickSightSpacing | None = None
