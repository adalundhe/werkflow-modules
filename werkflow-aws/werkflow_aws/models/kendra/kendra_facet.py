from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraFacet(BaseModel):
    DocumentAttributeKey: StrictStr | None = None
    Facets: list[KendraFacet] | None = None
    MaxResults: StrictInt | None = None
