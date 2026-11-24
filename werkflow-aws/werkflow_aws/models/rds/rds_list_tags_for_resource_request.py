from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_filter import RDSFilter


class RDSListTagsForResourceRequest(BaseModel):
    ResourceName: StrictStr
    Filters: list[RDSFilter] | None = None
