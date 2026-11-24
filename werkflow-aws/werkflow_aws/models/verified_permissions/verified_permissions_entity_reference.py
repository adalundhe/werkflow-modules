from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsEntityReference(BaseModel):
    unspecified: StrictBool | None = None
    identifier: VerifiedPermissionsEntityIdentifier | None = None
