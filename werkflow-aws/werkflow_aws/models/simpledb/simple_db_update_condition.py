from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SimpleDBUpdateCondition(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Exists: StrictBool | None = None
