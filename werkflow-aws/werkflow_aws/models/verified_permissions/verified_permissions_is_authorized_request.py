from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_action_identifier import VerifiedPermissionsActionIdentifier
from .verified_permissions_context_definition import VerifiedPermissionsContextDefinition
from .verified_permissions_entities_definition import VerifiedPermissionsEntitiesDefinition
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsIsAuthorizedRequest(BaseModel):
    policyStoreId: StrictStr
    principal: VerifiedPermissionsEntityIdentifier | None = None
    action: VerifiedPermissionsActionIdentifier | None = None
    resource: VerifiedPermissionsEntityIdentifier | None = None
    context: VerifiedPermissionsContextDefinition | None = None
    entities: VerifiedPermissionsEntitiesDefinition | None = None
