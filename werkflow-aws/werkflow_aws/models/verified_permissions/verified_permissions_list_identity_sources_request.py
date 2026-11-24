from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .verified_permissions_identity_source_filter import VerifiedPermissionsIdentitySourceFilter


class VerifiedPermissionsListIdentitySourcesRequest(BaseModel):
    policyStoreId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    filters: list[VerifiedPermissionsIdentitySourceFilter] | None = None
