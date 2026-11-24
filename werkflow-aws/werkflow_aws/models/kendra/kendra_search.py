from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KendraSearch(BaseModel):
    Facetable: StrictBool | None = None
    Searchable: StrictBool | None = None
    Displayable: StrictBool | None = None
    Sortable: StrictBool | None = None
