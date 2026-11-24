from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .eks_cluster_model import EKSClusterModel


class EKSDeregisterClusterResponse(BaseModel):
    cluster: EKSClusterModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
