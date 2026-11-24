from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_inventory_group import SSMInventoryGroup


class SSMInventoryAggregator(BaseModel):
    Expression: StrictStr | None = None
    Aggregators: list[SSMInventoryAggregator] | None = None
    Groups: list[SSMInventoryGroup] | None = None
