from __future__ import annotations
from pydantic import BaseModel
from .data_zone_asset_type_item import DataZoneAssetTypeItem
from .data_zone_form_type_data import DataZoneFormTypeData
from .data_zone_lineage_node_type_item import DataZoneLineageNodeTypeItem


class DataZoneSearchTypesResultItem(BaseModel):
    assetTypeItem: DataZoneAssetTypeItem | None = None
    formTypeItem: DataZoneFormTypeData | None = None
    lineageNodeTypeItem: DataZoneLineageNodeTypeItem | None = None
