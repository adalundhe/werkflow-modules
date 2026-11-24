from __future__ import annotations
from pydantic import BaseModel
from .eks_update_ack_config import EKSUpdateAckConfig
from .eks_update_argo_cd_config import EKSUpdateArgoCdConfig


class EKSUpdateCapabilityConfiguration(BaseModel):
    argoCd: EKSUpdateArgoCdConfig | None = None
    ack: EKSUpdateAckConfig | None = None
