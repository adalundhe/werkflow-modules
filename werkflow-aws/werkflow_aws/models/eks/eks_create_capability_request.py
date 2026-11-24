from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .eks_capability_configuration_request import EKSCapabilityConfigurationRequest


class EKSCreateCapabilityRequest(BaseModel):
    capabilityName: StrictStr
    clusterName: StrictStr
    type: Literal['ACK', 'KRO', 'ARGOCD']
    roleArn: StrictStr
    deletePropagationPolicy: Literal['RETAIN']
    clientRequestToken: StrictStr | None = None
    configuration: EKSCapabilityConfigurationRequest | None = None
    tags: dict[StrictStr, StrictStr] | None = None
