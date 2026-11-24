from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_service_node_port_range import EKSServiceNodePortRange


class EKSKubeApiServerConfigRequest(BaseModel):
    eventTtl: StrictStr | None = None
    serviceNodePortRange: EKSServiceNodePortRange | None = None
