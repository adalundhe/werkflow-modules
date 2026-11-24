from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_network_insights_access_scope_analysis import EC2NetworkInsightsAccessScopeAnalysis


class EC2StartNetworkInsightsAccessScopeAnalysisResponse(BaseModel):
    NetworkInsightsAccessScopeAnalysis: EC2NetworkInsightsAccessScopeAnalysis | None = None
    ResponseMetadata: dict[str, Any] | None = None
