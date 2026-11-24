from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_asset_property_timestamp import IoTAssetPropertyTimestamp
from .io_t_asset_property_variant import IoTAssetPropertyVariant


class IoTAssetPropertyValue(BaseModel):
    value: IoTAssetPropertyVariant | None = None
    timestamp: IoTAssetPropertyTimestamp | None = None
    quality: StrictStr | None = None
