from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListDevEndpointsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
