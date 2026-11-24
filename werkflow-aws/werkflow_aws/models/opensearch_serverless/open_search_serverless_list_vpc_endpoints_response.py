from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_serverless_vpc_endpoint_summary import OpenSearchServerlessVpcEndpointSummary


class OpenSearchServerlessListVpcEndpointsResponse(BaseModel):
    vpcEndpointSummaries: list[OpenSearchServerlessVpcEndpointSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
