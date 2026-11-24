from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchAddReplicationPeerRequest(BaseModel):
    DomainName: StrictStr
    PeerDomainArn: StrictStr
    DryRun: StrictBool | None = None
