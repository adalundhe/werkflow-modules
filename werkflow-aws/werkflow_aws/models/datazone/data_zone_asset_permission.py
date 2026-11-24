from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_permissions import DataZonePermissions


class DataZoneAssetPermission(BaseModel):
    assetId: StrictStr
    permissions: DataZonePermissions
