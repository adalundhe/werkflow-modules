from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchSwitchoverReplicationRequest(BaseModel):
    DomainName: StrictStr
    PeerDomainArn: StrictStr
