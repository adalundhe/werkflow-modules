from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_inventory_item_attribute import SSMInventoryItemAttribute


class SSMInventoryItemSchema(BaseModel):
    TypeName: StrictStr | None = None
    Version: StrictStr | None = None
    Attributes: list[SSMInventoryItemAttribute] | None = None
    DisplayName: StrictStr | None = None
