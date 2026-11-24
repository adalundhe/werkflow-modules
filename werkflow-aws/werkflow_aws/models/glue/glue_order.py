from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueOrder(BaseModel):
    Column: StrictStr | None = None
    SortOrder: StrictInt | None = None
