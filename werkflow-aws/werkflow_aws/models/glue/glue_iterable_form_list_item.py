from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIterableFormListItem(BaseModel):
    ItemId: StrictStr | None = None
    ItemName: StrictStr | None = None
    Description: StrictStr | None = None
    GlossaryTerms: list[StrictStr] | None = None
