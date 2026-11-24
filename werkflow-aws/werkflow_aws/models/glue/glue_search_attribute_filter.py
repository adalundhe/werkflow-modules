from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_search_filter_value import GlueSearchFilterValue


class GlueSearchAttributeFilter(BaseModel):
    Attribute: StrictStr
    Comparator: Literal['EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUALS', 'LESS_THAN', 'LESS_THAN_OR_EQUALS', 'NOT_EXISTS'] | None = None
    Value: GlueSearchFilterValue | None = None
