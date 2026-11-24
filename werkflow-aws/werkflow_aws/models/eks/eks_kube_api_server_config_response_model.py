from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_service_node_port_range_model import EKSServiceNodePortRangeModel


class EKSKubeApiServerConfigResponseModel(BaseModel):
    eventTtl: StrictStr | None = None
    serviceNodePortRange: EKSServiceNodePortRangeModel | None = None
