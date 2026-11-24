from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetConnectionGroupByRoutingEndpointRequest(BaseModel):
    RoutingEndpoint: StrictStr
