from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_inventory_result_entity import SSMInventoryResultEntity


class SSMGetInventoryResponse(BaseModel):
    Entities: list[SSMInventoryResultEntity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
