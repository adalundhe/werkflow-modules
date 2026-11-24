from __future__ import annotations
from pydantic import BaseModel
from .eks_remote_node_network import EKSRemoteNodeNetwork
from .eks_remote_pod_network import EKSRemotePodNetwork


class EKSRemoteNetworkConfigResponse(BaseModel):
    remoteNodeNetworks: list[EKSRemoteNodeNetwork] | None = None
    remotePodNetworks: list[EKSRemotePodNetwork] | None = None
