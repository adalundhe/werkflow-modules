from __future__ import annotations
from pydantic import BaseModel
from .eks_duration_parameter_config import EKSDurationParameterConfig
from .eks_port_range_parameter_config import EKSPortRangeParameterConfig


class EKSKubeApiServerVersionConfig(BaseModel):
    eventTtl: EKSDurationParameterConfig | None = None
    serviceNodePortRange: EKSPortRangeParameterConfig | None = None
