from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_access_scope_analysis_finding import EC2AccessScopeAnalysisFinding


class EC2GetNetworkInsightsAccessScopeAnalysisFindingsResponse(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: StrictStr | None = None
    AnalysisStatus: StrictStr | None = None
    AnalysisFindings: list[EC2AccessScopeAnalysisFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
