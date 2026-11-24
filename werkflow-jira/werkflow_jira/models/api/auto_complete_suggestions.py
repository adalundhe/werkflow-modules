from __future__ import annotations
from pydantic import BaseModel
from .auto_complete_suggestion import AutoCompleteSuggestion


class AutoCompleteSuggestions(BaseModel):
    results: list[AutoCompleteSuggestion] | None = None
