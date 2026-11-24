from __future__ import annotations
from pydantic import BaseModel
from .verified_permissions_kms_encryption_state import VerifiedPermissionsKmsEncryptionState
from .verified_permissions_unit import VerifiedPermissionsUnit


class VerifiedPermissionsEncryptionState(BaseModel):
    kmsEncryptionState: VerifiedPermissionsKmsEncryptionState | None = None
    default: VerifiedPermissionsUnit | None = None
