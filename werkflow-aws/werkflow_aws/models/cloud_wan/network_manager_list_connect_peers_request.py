from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerListConnectPeersRequest(BaseModel):
    CoreNetworkId: StrictStr | None = None
    ConnectAttachmentId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
