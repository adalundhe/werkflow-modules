from __future__ import annotations
from pydantic import BaseModel
from .verified_permissions_update_static_policy_definition import VerifiedPermissionsUpdateStaticPolicyDefinition


class VerifiedPermissionsUpdatePolicyDefinition(BaseModel):
    static: VerifiedPermissionsUpdateStaticPolicyDefinition | None = None
