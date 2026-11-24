from __future__ import annotations
from pydantic import BaseModel
from .kendra_text_with_highlights import KendraTextWithHighlights


class KendraAdditionalResultAttributeValue(BaseModel):
    TextWithHighlightsValue: KendraTextWithHighlights | None = None
