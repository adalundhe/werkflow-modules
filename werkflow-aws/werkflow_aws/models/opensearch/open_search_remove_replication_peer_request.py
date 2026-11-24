from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchRemoveReplicationPeerRequest(BaseModel):
    DomainName: StrictStr
    PeerDomainArn: StrictStr
