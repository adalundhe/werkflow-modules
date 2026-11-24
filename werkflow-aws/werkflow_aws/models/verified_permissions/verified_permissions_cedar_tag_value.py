from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsCedarTagValue(BaseModel):
    boolean: StrictBool | None = None
    entityIdentifier: VerifiedPermissionsEntityIdentifier | None = None
    long: StrictInt | None = None
    string: StrictStr | None = None
    set: list[VerifiedPermissionsCedarTagValue] | None = None
    record: dict[StrictStr, VerifiedPermissionsCedarTagValue] | None = None
    ipaddr: StrictStr | None = None
    decimal: StrictStr | None = None
    datetime: StrictStr | None = None
    duration: StrictStr | None = None
