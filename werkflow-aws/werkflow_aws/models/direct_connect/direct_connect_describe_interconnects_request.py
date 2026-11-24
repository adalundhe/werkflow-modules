from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectDescribeInterconnectsRequest(BaseModel):
    interconnectId: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
