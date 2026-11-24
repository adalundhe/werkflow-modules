from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_aggregator import SSMOpsAggregator
from .ssm_ops_filter import SSMOpsFilter
from .ssm_ops_result_attribute import SSMOpsResultAttribute


class SSMGetOpsSummaryRequest(BaseModel):
    SyncName: StrictStr | None = None
    Filters: list[SSMOpsFilter] | None = None
    Aggregators: list[SSMOpsAggregator] | None = None
    ResultAttributes: list[SSMOpsResultAttribute] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
