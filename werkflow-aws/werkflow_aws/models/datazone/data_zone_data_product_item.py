from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDataProductItem(BaseModel):
    itemType: StrictStr | None = None
    identifier: StrictStr | None = None
    revision: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
