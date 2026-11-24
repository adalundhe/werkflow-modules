from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueSearchFilterValue(BaseModel):
    StringValue: StrictStr | None = None
    LongValue: StrictInt | None = None
