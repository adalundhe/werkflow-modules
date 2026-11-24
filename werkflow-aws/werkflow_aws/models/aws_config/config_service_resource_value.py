from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceResourceValue(BaseModel):
    Value: StrictStr | None = None
