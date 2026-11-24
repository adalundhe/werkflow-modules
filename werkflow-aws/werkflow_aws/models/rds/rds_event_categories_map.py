from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSEventCategoriesMap(BaseModel):
    SourceType: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
