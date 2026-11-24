from __future__ import annotations
from pydantic import BaseModel
from .eks_node_resources_fit_version_config import EKSNodeResourcesFitVersionConfig


class EKSKubeSchedulerVersionConfig(BaseModel):
    nodeResourcesFit: EKSNodeResourcesFitVersionConfig | None = None
