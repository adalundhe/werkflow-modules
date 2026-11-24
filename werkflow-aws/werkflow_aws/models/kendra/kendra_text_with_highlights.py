from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_highlight import KendraHighlight


class KendraTextWithHighlights(BaseModel):
    Text: StrictStr | None = None
    Highlights: list[KendraHighlight] | None = None
