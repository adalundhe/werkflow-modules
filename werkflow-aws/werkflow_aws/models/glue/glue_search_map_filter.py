from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_search_map_filter_value import GlueSearchMapFilterValue


class GlueSearchMapFilter(BaseModel):
    Attribute: StrictStr
    Key: StrictStr
    Value: GlueSearchMapFilterValue
