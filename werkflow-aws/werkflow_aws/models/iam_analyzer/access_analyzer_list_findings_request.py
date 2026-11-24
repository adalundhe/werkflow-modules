from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .access_analyzer_criterion import AccessAnalyzerCriterion
from .access_analyzer_sort_criteria import AccessAnalyzerSortCriteria


class AccessAnalyzerListFindingsRequest(BaseModel):
    analyzerArn: StrictStr
    filter: dict[StrictStr, AccessAnalyzerCriterion] | None = None
    sort: AccessAnalyzerSortCriteria | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
