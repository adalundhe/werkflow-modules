from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_ops_filter import SSMOpsFilter


class SSMOpsAggregator(BaseModel):
    AggregatorType: StrictStr | None = None
    TypeName: StrictStr | None = None
    AttributeName: StrictStr | None = None
    Values: dict[StrictStr, StrictStr] | None = None
    Filters: list[SSMOpsFilter] | None = None
    Aggregators: list[SSMOpsAggregator] | None = None
