from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_filter_value import GlueFilterValue


class GlueFilterExpression(BaseModel):
    Operation: StrictStr | None = None
    Negated: StrictBool | None = None
    Values: list[GlueFilterValue] | None = None
