from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_accepted_asset_scope import DataZoneAcceptedAssetScope
from .data_zone_asset_permission import DataZoneAssetPermission


class DataZoneAcceptSubscriptionRequestRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    decisionComment: StrictStr | None = None
    assetScopes: list[DataZoneAcceptedAssetScope] | None = None
    assetPermissions: list[DataZoneAssetPermission] | None = None
