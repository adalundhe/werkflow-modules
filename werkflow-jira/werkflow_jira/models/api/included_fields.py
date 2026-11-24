from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IncludedFields(BaseModel):
    actuallyIncluded: list[StrictStr] | None = None
    excluded: list[StrictStr] | None = None
    included: list[StrictStr] | None = None
