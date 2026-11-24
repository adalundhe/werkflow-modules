from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .verified_permissions_configuration_item import VerifiedPermissionsConfigurationItem
from .verified_permissions_identity_source_item_details import VerifiedPermissionsIdentitySourceItemDetails


class VerifiedPermissionsIdentitySourceItem(BaseModel):
    createdDate: datetime.datetime | StrictStr | None = None
    details: VerifiedPermissionsIdentitySourceItemDetails | None = None
    identitySourceId: StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    policyStoreId: StrictStr | None = None
    principalEntityType: StrictStr | None = None
    configuration: VerifiedPermissionsConfigurationItem | None = None
