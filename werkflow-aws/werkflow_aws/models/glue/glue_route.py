from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_group_filters import GlueGroupFilters


class GlueRoute(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    GroupFiltersList: list[GlueGroupFilters] | None = None
