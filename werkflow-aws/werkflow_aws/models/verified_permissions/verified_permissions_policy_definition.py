from __future__ import annotations
from pydantic import BaseModel
from .verified_permissions_static_policy_definition import VerifiedPermissionsStaticPolicyDefinition
from .verified_permissions_template_linked_policy_definition import VerifiedPermissionsTemplateLinkedPolicyDefinition


class VerifiedPermissionsPolicyDefinition(BaseModel):
    static: VerifiedPermissionsStaticPolicyDefinition | None = None
    templateLinked: VerifiedPermissionsTemplateLinkedPolicyDefinition | None = None
