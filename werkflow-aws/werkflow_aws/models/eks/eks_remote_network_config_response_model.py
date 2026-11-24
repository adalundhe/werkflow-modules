from __future__ import annotations
from pydantic import BaseModel
from .eks_remote_node_network_model import EKSRemoteNodeNetworkModel
from .eks_remote_pod_network_model import EKSRemotePodNetworkModel


class EKSRemoteNetworkConfigResponseModel(BaseModel):
    remoteNodeNetworks: list[EKSRemoteNodeNetworkModel] | None = None
    remotePodNetworks: list[EKSRemotePodNetworkModel] | None = None
