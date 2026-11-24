from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsTemplateLinkedPolicyDefinition(BaseModel):
    policyTemplateId: StrictStr
    principal: VerifiedPermissionsEntityIdentifier | None = None
    resource: VerifiedPermissionsEntityIdentifier | None = None
