from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_aggregate_operation import GlueAggregateOperation


class GlueAggregate(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Groups: list[list[StrictStr]] | None = None
    Aggs: list[GlueAggregateOperation] | None = None
