from __future__ import annotations
from pydantic import BaseModel
from .eks_node_resources_fit_config_model import EKSNodeResourcesFitConfigModel


class EKSKubeSchedulerConfigResponseModel(BaseModel):
    nodeResourcesFit: EKSNodeResourcesFitConfigModel | None = None
