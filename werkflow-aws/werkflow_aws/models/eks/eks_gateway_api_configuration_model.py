from __future__ import annotations
from pydantic import BaseModel
from .eks_crd_management_configuration_model import EKSCrdManagementConfigurationModel


class EKSGatewayApiConfigurationModel(BaseModel):
    crds: EKSCrdManagementConfigurationModel | None = None
