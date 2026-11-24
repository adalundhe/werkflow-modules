from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_insights_access_scope_analysis import EC2NetworkInsightsAccessScopeAnalysis


class EC2DescribeNetworkInsightsAccessScopeAnalysesResponse(BaseModel):
    NetworkInsightsAccessScopeAnalyses: list[EC2NetworkInsightsAccessScopeAnalysis] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
