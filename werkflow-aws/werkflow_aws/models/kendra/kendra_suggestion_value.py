from __future__ import annotations
from pydantic import BaseModel
from .kendra_suggestion_text_with_highlights import KendraSuggestionTextWithHighlights


class KendraSuggestionValue(BaseModel):
    Text: KendraSuggestionTextWithHighlights | None = None
