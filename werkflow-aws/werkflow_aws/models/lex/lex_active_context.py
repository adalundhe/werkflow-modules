from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexActiveContext(BaseModel):
    name: StrictStr | None = None
