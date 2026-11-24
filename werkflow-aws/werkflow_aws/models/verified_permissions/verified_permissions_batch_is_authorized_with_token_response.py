from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .verified_permissions_batch_is_authorized_with_token_output_item import VerifiedPermissionsBatchIsAuthorizedWithTokenOutputItem
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsBatchIsAuthorizedWithTokenResponse(BaseModel):
    principal: VerifiedPermissionsEntityIdentifier | None = None
    results: list[VerifiedPermissionsBatchIsAuthorizedWithTokenOutputItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
