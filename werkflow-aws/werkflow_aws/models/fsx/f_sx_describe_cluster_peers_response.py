from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_cluster_peer import FSxClusterPeer


class FSxDescribeClusterPeersResponse(BaseModel):
    ClusterPeers: list[FSxClusterPeer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
