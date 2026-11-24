from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_suggestion_highlight import KendraSuggestionHighlight


class KendraSuggestionTextWithHighlights(BaseModel):
    Text: StrictStr | None = None
    Highlights: list[KendraSuggestionHighlight] | None = None
