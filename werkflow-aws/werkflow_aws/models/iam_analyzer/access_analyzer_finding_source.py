from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_finding_source_detail import AccessAnalyzerFindingSourceDetail


class AccessAnalyzerFindingSource(BaseModel):
    type: StrictStr | None = None
    detail: AccessAnalyzerFindingSourceDetail | None = None
