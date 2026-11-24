from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_configuration import VerifiedPermissionsConfiguration


class VerifiedPermissionsCreateIdentitySourceRequest(BaseModel):
    policyStoreId: StrictStr
    configuration: VerifiedPermissionsConfiguration
    clientToken: StrictStr | None = None
    principalEntityType: StrictStr | None = None
