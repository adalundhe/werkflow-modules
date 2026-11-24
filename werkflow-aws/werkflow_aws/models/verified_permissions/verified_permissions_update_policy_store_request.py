from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .verified_permissions_validation_settings import VerifiedPermissionsValidationSettings


class VerifiedPermissionsUpdatePolicyStoreRequest(BaseModel):
    policyStoreId: StrictStr
    validationSettings: VerifiedPermissionsValidationSettings
    deletionProtection: Literal['ENABLED', 'DISABLED'] | None = None
    description: StrictStr | None = None
