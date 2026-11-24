from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListVpcEndpointsRequest(BaseModel):
    NextToken: StrictStr | None = None
