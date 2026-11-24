from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_serverless_vpc_endpoint_filters import OpenSearchServerlessVpcEndpointFilters


class OpenSearchServerlessListVpcEndpointsRequest(BaseModel):
    vpcEndpointFilters: OpenSearchServerlessVpcEndpointFilters | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
