from __future__ import annotations
from pydantic import BaseModel
from .eks_port_range_constraints import EKSPortRangeConstraints
from .eks_service_node_port_range_model import EKSServiceNodePortRangeModel


class EKSPortRangeParameterConfig(BaseModel):
    defaultValue: EKSServiceNodePortRangeModel | None = None
    constraints: EKSPortRangeConstraints | None = None
