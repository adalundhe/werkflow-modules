from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_batch_is_authorized_with_token_input_item import VerifiedPermissionsBatchIsAuthorizedWithTokenInputItem
from .verified_permissions_entities_definition import VerifiedPermissionsEntitiesDefinition


class VerifiedPermissionsBatchIsAuthorizedWithTokenRequest(BaseModel):
    policyStoreId: StrictStr
    requests: list[VerifiedPermissionsBatchIsAuthorizedWithTokenInputItem]
    identityToken: StrictStr | None = None
    accessToken: StrictStr | None = None
    entities: VerifiedPermissionsEntitiesDefinition | None = None
