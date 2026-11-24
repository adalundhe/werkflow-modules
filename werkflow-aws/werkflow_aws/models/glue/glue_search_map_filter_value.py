from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSearchMapFilterValue(BaseModel):
    StringValue: StrictStr | None = None
