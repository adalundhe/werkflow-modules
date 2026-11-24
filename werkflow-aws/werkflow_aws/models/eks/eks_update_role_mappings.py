from __future__ import annotations
from pydantic import BaseModel
from .eks_argo_cd_role_mapping import EKSArgoCdRoleMapping


class EKSUpdateRoleMappings(BaseModel):
    addOrUpdateRoleMappings: list[EKSArgoCdRoleMapping] | None = None
    removeRoleMappings: list[EKSArgoCdRoleMapping] | None = None
