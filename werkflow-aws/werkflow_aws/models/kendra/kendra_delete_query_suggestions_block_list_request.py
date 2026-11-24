from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteQuerySuggestionsBlockListRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
