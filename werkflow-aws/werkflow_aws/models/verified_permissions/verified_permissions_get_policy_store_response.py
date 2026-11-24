from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_encryption_state import VerifiedPermissionsEncryptionState
from .verified_permissions_validation_settings import VerifiedPermissionsValidationSettings


class VerifiedPermissionsGetPolicyStoreResponse(BaseModel):
    policyStoreId: StrictStr | None = None
    arn: StrictStr | None = None
    validationSettings: VerifiedPermissionsValidationSettings | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    deletionProtection: StrictStr | None = None
    encryptionState: VerifiedPermissionsEncryptionState | None = None
    cedarVersion: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
