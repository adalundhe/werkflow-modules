from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_inventory_result_item import SSMInventoryResultItem


class SSMInventoryResultEntity(BaseModel):
    Id: StrictStr | None = None
    Data: dict[StrictStr, SSMInventoryResultItem] | None = None
