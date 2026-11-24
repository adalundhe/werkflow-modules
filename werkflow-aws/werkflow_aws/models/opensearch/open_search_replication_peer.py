from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchReplicationPeer(BaseModel):
    PeerDomainArn: StrictStr | None = None
    PeerRole: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
