from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .verified_permissions_encryption_settings import VerifiedPermissionsEncryptionSettings
from .verified_permissions_validation_settings import VerifiedPermissionsValidationSettings


class VerifiedPermissionsCreatePolicyStoreRequest(BaseModel):
    validationSettings: VerifiedPermissionsValidationSettings
    clientToken: StrictStr | None = None
    description: StrictStr | None = None
    deletionProtection: Literal['ENABLED', 'DISABLED'] | None = None
    encryptionSettings: VerifiedPermissionsEncryptionSettings | None = None
    tags: dict[StrictStr, StrictStr] | None = None
