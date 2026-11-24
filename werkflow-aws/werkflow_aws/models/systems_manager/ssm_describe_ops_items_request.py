from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_filter import SSMOpsItemFilter


class SSMDescribeOpsItemsRequest(BaseModel):
    OpsItemFilters: list[SSMOpsItemFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
