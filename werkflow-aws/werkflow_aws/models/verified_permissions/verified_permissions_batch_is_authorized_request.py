from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_batch_is_authorized_input_item import VerifiedPermissionsBatchIsAuthorizedInputItem
from .verified_permissions_entities_definition import VerifiedPermissionsEntitiesDefinition


class VerifiedPermissionsBatchIsAuthorizedRequest(BaseModel):
    policyStoreId: StrictStr
    requests: list[VerifiedPermissionsBatchIsAuthorizedInputItem]
    entities: VerifiedPermissionsEntitiesDefinition | None = None
