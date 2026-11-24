from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_network_insights_access_scope import EC2NetworkInsightsAccessScope


class EC2DescribeNetworkInsightsAccessScopesResponse(BaseModel):
    NetworkInsightsAccessScopes: list[EC2NetworkInsightsAccessScope] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
