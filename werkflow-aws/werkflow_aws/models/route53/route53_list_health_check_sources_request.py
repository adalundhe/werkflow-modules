from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListHealthCheckSourcesRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictStr | None = None
