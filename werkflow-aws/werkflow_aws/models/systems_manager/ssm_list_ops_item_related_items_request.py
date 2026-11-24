from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_related_items_filter import SSMOpsItemRelatedItemsFilter


class SSMListOpsItemRelatedItemsRequest(BaseModel):
    OpsItemId: StrictStr | None = None
    Filters: list[SSMOpsItemRelatedItemsFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
