from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_divergent_item import OpenSearchDivergentItem


class OpenSearchDiffItems(BaseModel):
    SourceOnly: list[StrictStr] | None = None
    TargetOnly: list[StrictStr] | None = None
    Diverged: list[OpenSearchDivergentItem] | None = None
