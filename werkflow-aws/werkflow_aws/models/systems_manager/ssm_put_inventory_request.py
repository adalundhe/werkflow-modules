from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_inventory_item import SSMInventoryItem


class SSMPutInventoryRequest(BaseModel):
    InstanceId: StrictStr
    Items: list[SSMInventoryItem]
