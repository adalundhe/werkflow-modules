from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_update_configuration import VerifiedPermissionsUpdateConfiguration


class VerifiedPermissionsUpdateIdentitySourceRequest(BaseModel):
    policyStoreId: StrictStr
    identitySourceId: StrictStr
    updateConfiguration: VerifiedPermissionsUpdateConfiguration
    principalEntityType: StrictStr | None = None
