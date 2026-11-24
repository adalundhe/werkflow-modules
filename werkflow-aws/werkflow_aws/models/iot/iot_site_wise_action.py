from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_put_asset_property_value_entry import IoTPutAssetPropertyValueEntry


class IotSiteWiseAction(BaseModel):
    putAssetPropertyValueEntries: list[IoTPutAssetPropertyValueEntry] | None = None
    roleArn: StrictStr | None = None
