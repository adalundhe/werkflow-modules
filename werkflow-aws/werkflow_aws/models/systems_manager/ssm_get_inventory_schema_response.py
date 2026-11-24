from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_inventory_item_schema import SSMInventoryItemSchema


class SSMGetInventorySchemaResponse(BaseModel):
    Schemas: list[SSMInventoryItemSchema] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
