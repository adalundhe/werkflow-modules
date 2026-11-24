from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_asset_scope import DataZoneAssetScope
from .data_zone_failure_cause import DataZoneFailureCause
from .data_zone_permissions import DataZonePermissions


class DataZoneSubscribedAsset(BaseModel):
    assetId: StrictStr | None = None
    assetRevision: StrictStr | None = None
    status: StrictStr | None = None
    targetName: StrictStr | None = None
    failureCause: DataZoneFailureCause | None = None
    grantedTimestamp: datetime.datetime | StrictStr | None = None
    failureTimestamp: datetime.datetime | StrictStr | None = None
    assetScope: DataZoneAssetScope | None = None
    permissions: DataZonePermissions | None = None
