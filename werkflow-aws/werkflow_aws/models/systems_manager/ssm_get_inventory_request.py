from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_inventory_aggregator import SSMInventoryAggregator
from .ssm_inventory_filter import SSMInventoryFilter
from .ssm_result_attribute import SSMResultAttribute


class SSMGetInventoryRequest(BaseModel):
    Filters: list[SSMInventoryFilter] | None = None
    Aggregators: list[SSMInventoryAggregator] | None = None
    ResultAttributes: list[SSMResultAttribute] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
