from __future__ import annotations
from pydantic import BaseModel
from .data_zone_asset_item import DataZoneAssetItem
from .data_zone_data_product_result_item import DataZoneDataProductResultItem
from .data_zone_glossary_item import DataZoneGlossaryItem
from .data_zone_glossary_term_item import DataZoneGlossaryTermItem


class DataZoneSearchInventoryResultItem(BaseModel):
    glossaryItem: DataZoneGlossaryItem | None = None
    glossaryTermItem: DataZoneGlossaryTermItem | None = None
    assetItem: DataZoneAssetItem | None = None
    dataProductItem: DataZoneDataProductResultItem | None = None
