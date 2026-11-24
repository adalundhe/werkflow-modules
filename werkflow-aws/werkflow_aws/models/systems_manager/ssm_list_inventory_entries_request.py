from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_inventory_filter import SSMInventoryFilter


class SSMListInventoryEntriesRequest(BaseModel):
    InstanceId: StrictStr
    TypeName: StrictStr
    Filters: list[SSMInventoryFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
