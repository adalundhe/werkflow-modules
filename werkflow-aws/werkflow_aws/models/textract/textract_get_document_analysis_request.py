from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TextractGetDocumentAnalysisRequest(BaseModel):
    JobId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
