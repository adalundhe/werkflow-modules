from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoCompleteSuggestion(BaseModel):
    displayName: StrictStr | None = None
    value: StrictStr | None = None
