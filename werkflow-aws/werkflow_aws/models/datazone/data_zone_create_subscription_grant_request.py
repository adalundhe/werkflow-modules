from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_asset_target_name_map import DataZoneAssetTargetNameMap
from .data_zone_granted_entity_input import DataZoneGrantedEntityInput


class DataZoneCreateSubscriptionGrantRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    grantedEntity: DataZoneGrantedEntityInput
    subscriptionTargetIdentifier: StrictStr | None = None
    assetTargetNames: list[DataZoneAssetTargetNameMap] | None = None
    clientToken: StrictStr | None = None
