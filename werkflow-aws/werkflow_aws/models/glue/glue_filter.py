from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_filter_expression import GlueFilterExpression


class GlueFilter(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    LogicalOperator: StrictStr | None = None
    Filters: list[GlueFilterExpression] | None = None
