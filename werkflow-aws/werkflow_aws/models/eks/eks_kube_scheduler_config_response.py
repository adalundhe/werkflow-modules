from __future__ import annotations
from pydantic import BaseModel
from .eks_node_resources_fit_config import EKSNodeResourcesFitConfig


class EKSKubeSchedulerConfigResponse(BaseModel):
    nodeResourcesFit: EKSNodeResourcesFitConfig | None = None
