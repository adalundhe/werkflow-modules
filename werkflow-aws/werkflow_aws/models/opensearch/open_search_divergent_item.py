from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_divergent_field import OpenSearchDivergentField


class OpenSearchDivergentItem(BaseModel):
    Name: StrictStr | None = None
    Fields: list[OpenSearchDivergentField] | None = None
