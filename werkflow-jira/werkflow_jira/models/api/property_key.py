from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PropertyKey(BaseModel):
    key: StrictStr | None = None
    self: StrictStr | None = None
