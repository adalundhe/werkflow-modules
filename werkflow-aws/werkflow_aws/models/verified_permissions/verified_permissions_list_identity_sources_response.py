from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_identity_source_item import VerifiedPermissionsIdentitySourceItem


class VerifiedPermissionsListIdentitySourcesResponse(BaseModel):
    nextToken: StrictStr | None = None
    identitySources: list[VerifiedPermissionsIdentitySourceItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
