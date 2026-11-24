from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFilterValue(BaseModel):
    Type: StrictStr | None = None
    Value: list[StrictStr] | None = None
