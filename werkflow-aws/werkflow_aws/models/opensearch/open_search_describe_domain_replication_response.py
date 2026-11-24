from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_replication_peer import OpenSearchReplicationPeer


class OpenSearchDescribeDomainReplicationResponse(BaseModel):
    DomainArn: StrictStr | None = None
    Role: StrictStr | None = None
    Peers: list[OpenSearchReplicationPeer] | None = None
    ResponseMetadata: dict[str, Any] | None = None
