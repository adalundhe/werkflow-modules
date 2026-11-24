from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerListAccessPreviewsRequest(BaseModel):
    analyzerArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
