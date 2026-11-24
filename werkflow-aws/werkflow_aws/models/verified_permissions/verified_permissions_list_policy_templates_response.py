from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_policy_template_item import VerifiedPermissionsPolicyTemplateItem


class VerifiedPermissionsListPolicyTemplatesResponse(BaseModel):
    nextToken: StrictStr | None = None
    policyTemplates: list[VerifiedPermissionsPolicyTemplateItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
