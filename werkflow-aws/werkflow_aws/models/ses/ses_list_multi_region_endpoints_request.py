from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESListMultiRegionEndpointsRequest(BaseModel):
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
