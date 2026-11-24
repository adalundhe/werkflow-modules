from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TextractGetLendingAnalysisRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
