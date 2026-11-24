from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_inventory_destination import AWSS3InventoryDestination
from .awss3_inventory_filter import AWSS3InventoryFilter
from .awss3_inventory_schedule import AWSS3InventorySchedule


class AWSS3InventoryConfiguration(BaseModel):
    Destination: AWSS3InventoryDestination | None = None
    IsEnabled: StrictBool | None = None
    Filter: AWSS3InventoryFilter | None = None
    Id: StrictStr | None = None
    IncludedObjectVersions: StrictStr | None = None
    OptionalFields: list[StrictStr] | None = None
    Schedule: AWSS3InventorySchedule | None = None
