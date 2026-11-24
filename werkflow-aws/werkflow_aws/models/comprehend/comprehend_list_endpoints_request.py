from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_endpoint_filter import ComprehendEndpointFilter


class ComprehendListEndpointsRequest(BaseModel):
    Filter: ComprehendEndpointFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
