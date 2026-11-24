from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeQuerySuggestionsBlockListRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
