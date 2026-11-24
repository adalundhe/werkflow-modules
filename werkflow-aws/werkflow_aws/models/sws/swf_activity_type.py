from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFActivityType(BaseModel):
    name: StrictStr | None = None
    version: StrictStr | None = None
