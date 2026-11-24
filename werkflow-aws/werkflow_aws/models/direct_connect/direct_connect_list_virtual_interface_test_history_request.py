from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectListVirtualInterfaceTestHistoryRequest(BaseModel):
    testId: StrictStr | None = None
    virtualInterfaceId: StrictStr | None = None
    bgpPeers: list[StrictStr] | None = None
    status: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
