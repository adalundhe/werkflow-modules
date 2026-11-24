from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .eks_update_capability_configuration import EKSUpdateCapabilityConfiguration


class EKSUpdateCapabilityRequest(BaseModel):
    clusterName: StrictStr
    capabilityName: StrictStr
    roleArn: StrictStr | None = None
    configuration: EKSUpdateCapabilityConfiguration | None = None
    clientRequestToken: StrictStr | None = None
    deletePropagationPolicy: Literal['RETAIN'] | None = None
