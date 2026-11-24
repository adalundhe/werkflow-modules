from __future__ import annotations
from pydantic import BaseModel
from .eks_crd_management_configuration import EKSCrdManagementConfiguration


class EKSGatewayApiConfiguration(BaseModel):
    crds: EKSCrdManagementConfiguration | None = None
