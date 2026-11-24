from __future__ import annotations
from pydantic import BaseModel
from .verified_permissions_action_identifier import VerifiedPermissionsActionIdentifier
from .verified_permissions_context_definition import VerifiedPermissionsContextDefinition
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsBatchIsAuthorizedWithTokenInputItem(BaseModel):
    action: VerifiedPermissionsActionIdentifier | None = None
    resource: VerifiedPermissionsEntityIdentifier | None = None
    context: VerifiedPermissionsContextDefinition | None = None
