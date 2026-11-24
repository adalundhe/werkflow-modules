from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_asset_property_value import IoTAssetPropertyValue


class IoTPutAssetPropertyValueEntry(BaseModel):
    entryId: StrictStr | None = None
    assetId: StrictStr | None = None
    propertyId: StrictStr | None = None
    propertyAlias: StrictStr | None = None
    propertyValues: list[IoTAssetPropertyValue] | None = None
