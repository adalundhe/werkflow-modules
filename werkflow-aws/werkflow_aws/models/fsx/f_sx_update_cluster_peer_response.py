from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_cluster_peer import FSxClusterPeer


class FSxUpdateClusterPeerResponse(BaseModel):
    ClusterPeer: FSxClusterPeer | None = None
    ResponseMetadata: dict[str, Any] | None = None
