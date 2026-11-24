from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_asset_filter_configuration import DataZoneAssetFilterConfiguration


class DataZoneCreateAssetFilterRequest(BaseModel):
    domainIdentifier: StrictStr
    assetIdentifier: StrictStr
    name: StrictStr
    configuration: DataZoneAssetFilterConfiguration
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
