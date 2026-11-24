from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAllowedValue(BaseModel):
    Description: StrictStr | None = None
    Value: StrictStr | None = None
