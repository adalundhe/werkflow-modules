from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .verified_permissions_attribute_value import VerifiedPermissionsAttributeValue
from .verified_permissions_cedar_tag_value import VerifiedPermissionsCedarTagValue
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsEntityItem(BaseModel):
    identifier: VerifiedPermissionsEntityIdentifier
    attributes: dict[StrictStr, VerifiedPermissionsAttributeValue] | None = None
    parents: list[VerifiedPermissionsEntityIdentifier] | None = None
    tags: dict[StrictStr, VerifiedPermissionsCedarTagValue] | None = None
