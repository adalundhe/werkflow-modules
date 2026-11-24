from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_filter import NeptuneFilter


class NeptuneListTagsForResourceRequest(BaseModel):
    ResourceName: StrictStr
    Filters: list[NeptuneFilter] | None = None
