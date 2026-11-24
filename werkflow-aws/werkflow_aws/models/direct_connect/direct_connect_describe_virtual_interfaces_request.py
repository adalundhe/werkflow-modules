from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectDescribeVirtualInterfacesRequest(BaseModel):
    connectionId: StrictStr | None = None
    virtualInterfaceId: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
