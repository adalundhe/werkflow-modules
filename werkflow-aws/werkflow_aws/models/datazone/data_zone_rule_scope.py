from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .data_zone_asset_types_for_rule import DataZoneAssetTypesForRule
from .data_zone_projects_for_rule import DataZoneProjectsForRule


class DataZoneRuleScope(BaseModel):
    assetType: DataZoneAssetTypesForRule | None = None
    dataProduct: StrictBool | None = None
    project: DataZoneProjectsForRule | None = None
