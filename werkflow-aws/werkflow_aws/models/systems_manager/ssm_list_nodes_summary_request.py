from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_node_aggregator import SSMNodeAggregator
from .ssm_node_filter import SSMNodeFilter


class SSMListNodesSummaryRequest(BaseModel):
    Aggregators: list[SSMNodeAggregator]
    SyncName: StrictStr | None = None
    Filters: list[SSMNodeFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
