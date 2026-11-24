from __future__ import annotations
from pydantic import BaseModel
from .verified_permissions_kms_encryption_settings import VerifiedPermissionsKmsEncryptionSettings
from .verified_permissions_unit import VerifiedPermissionsUnit


class VerifiedPermissionsEncryptionSettings(BaseModel):
    kmsEncryptionSettings: VerifiedPermissionsKmsEncryptionSettings | None = None
    default: VerifiedPermissionsUnit | None = None
