from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .access_analyzer_criterion import AccessAnalyzerCriterion


class AccessAnalyzerListAccessPreviewFindingsRequest(BaseModel):
    accessPreviewId: StrictStr
    analyzerArn: StrictStr
    filter: dict[StrictStr, AccessAnalyzerCriterion] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
