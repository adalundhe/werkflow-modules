from __future__ import annotations
from pydantic import BaseModel
from .eks_argo_cd_network_access_config_request import EKSArgoCdNetworkAccessConfigRequest
from .eks_update_role_mappings import EKSUpdateRoleMappings


class EKSUpdateArgoCdConfig(BaseModel):
    rbacRoleMappings: EKSUpdateRoleMappings | None = None
    networkAccess: EKSArgoCdNetworkAccessConfigRequest | None = None
