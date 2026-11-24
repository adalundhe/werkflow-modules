from __future__ import annotations
from pydantic import BaseModel
from .eks_ack_config_request import EKSAckConfigRequest
from .eks_argo_cd_config_request import EKSArgoCdConfigRequest


class EKSCapabilityConfigurationRequest(BaseModel):
    argoCd: EKSArgoCdConfigRequest | None = None
    ack: EKSAckConfigRequest | None = None
