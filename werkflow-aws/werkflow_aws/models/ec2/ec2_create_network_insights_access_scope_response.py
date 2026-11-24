from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_network_insights_access_scope import EC2NetworkInsightsAccessScope
from .ec2_network_insights_access_scope_content import EC2NetworkInsightsAccessScopeContent


class EC2CreateNetworkInsightsAccessScopeResponse(BaseModel):
    NetworkInsightsAccessScope: EC2NetworkInsightsAccessScope | None = None
    NetworkInsightsAccessScopeContent: EC2NetworkInsightsAccessScopeContent | None = None
    ResponseMetadata: dict[str, Any] | None = None
