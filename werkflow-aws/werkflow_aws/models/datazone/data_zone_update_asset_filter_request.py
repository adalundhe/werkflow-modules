from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_asset_filter_configuration import DataZoneAssetFilterConfiguration


class DataZoneUpdateAssetFilterRequest(BaseModel):
    domainIdentifier: StrictStr
    assetIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    configuration: DataZoneAssetFilterConfiguration | None = None
