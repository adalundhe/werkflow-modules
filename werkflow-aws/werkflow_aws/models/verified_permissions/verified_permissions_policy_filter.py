from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .verified_permissions_entity_reference import VerifiedPermissionsEntityReference


class VerifiedPermissionsPolicyFilter(BaseModel):
    principal: VerifiedPermissionsEntityReference | None = None
    resource: VerifiedPermissionsEntityReference | None = None
    policyType: Literal['STATIC', 'TEMPLATE_LINKED'] | None = None
    policyTemplateId: StrictStr | None = None
