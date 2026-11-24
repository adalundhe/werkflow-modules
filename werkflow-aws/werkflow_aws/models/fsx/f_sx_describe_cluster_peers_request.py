from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_cluster_peer_filter import FSxClusterPeerFilter


class FSxDescribeClusterPeersRequest(BaseModel):
    ClusterPeerIds: list[StrictStr] | None = None
    Filters: list[FSxClusterPeerFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
