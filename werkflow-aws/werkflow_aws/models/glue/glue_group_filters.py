from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_filter_expression import GlueFilterExpression


class GlueGroupFilters(BaseModel):
    GroupName: StrictStr | None = None
    Filters: list[GlueFilterExpression] | None = None
    LogicalOperator: StrictStr | None = None
