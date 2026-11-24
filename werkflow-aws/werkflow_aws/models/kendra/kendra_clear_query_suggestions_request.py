from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraClearQuerySuggestionsRequest(BaseModel):
    IndexId: StrictStr
