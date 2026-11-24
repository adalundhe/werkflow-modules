from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeQuerySuggestionsConfigRequest(BaseModel):
    IndexId: StrictStr
