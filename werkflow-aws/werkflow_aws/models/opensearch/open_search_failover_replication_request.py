from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchFailoverReplicationRequest(BaseModel):
    DomainName: StrictStr
    PeerDomainArn: StrictStr
    AllowDataLoss: StrictBool
