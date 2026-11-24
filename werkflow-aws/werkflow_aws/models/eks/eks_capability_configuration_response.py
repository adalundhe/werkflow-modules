from __future__ import annotations
from pydantic import BaseModel
from .eks_ack_config_response import EKSAckConfigResponse
from .eks_argo_cd_config_response import EKSArgoCdConfigResponse


class EKSCapabilityConfigurationResponse(BaseModel):
    argoCd: EKSArgoCdConfigResponse | None = None
    ack: EKSAckConfigResponse | None = None
