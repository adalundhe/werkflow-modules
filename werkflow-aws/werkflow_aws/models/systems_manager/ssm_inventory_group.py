from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_inventory_filter import SSMInventoryFilter


class SSMInventoryGroup(BaseModel):
    Name: StrictStr
    Filters: list[SSMInventoryFilter]
