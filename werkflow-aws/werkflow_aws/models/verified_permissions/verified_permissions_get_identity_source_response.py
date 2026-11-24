from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .verified_permissions_configuration_detail import VerifiedPermissionsConfigurationDetail
from .verified_permissions_identity_source_details import VerifiedPermissionsIdentitySourceDetails


class VerifiedPermissionsGetIdentitySourceResponse(BaseModel):
    createdDate: datetime.datetime | StrictStr | None = None
    details: VerifiedPermissionsIdentitySourceDetails | None = None
    identitySourceId: StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    policyStoreId: StrictStr | None = None
    principalEntityType: StrictStr | None = None
    configuration: VerifiedPermissionsConfigurationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
