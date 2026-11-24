from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_action_identifier import VerifiedPermissionsActionIdentifier
from .verified_permissions_entity_identifier import VerifiedPermissionsEntityIdentifier


class VerifiedPermissionsCreatePolicyResponse(BaseModel):
    policyStoreId: StrictStr | None = None
    policyId: StrictStr | None = None
    policyType: StrictStr | None = None
    principal: VerifiedPermissionsEntityIdentifier | None = None
    resource: VerifiedPermissionsEntityIdentifier | None = None
    actions: list[VerifiedPermissionsActionIdentifier] | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    effect: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
