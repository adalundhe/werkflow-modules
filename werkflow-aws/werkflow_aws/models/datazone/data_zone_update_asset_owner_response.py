from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_asset_ownership_transfer import DataZoneAssetOwnershipTransfer


class DataZoneUpdateAssetOwnerResponse(BaseModel):
    id: StrictStr | None = None
    revision: StrictStr | None = None
    ownershipTransfer: DataZoneAssetOwnershipTransfer | None = None
    ResponseMetadata: dict[str, Any] | None = None
