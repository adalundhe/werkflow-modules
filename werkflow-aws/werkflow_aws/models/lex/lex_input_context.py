from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexInputContext(BaseModel):
    name: StrictStr | None = None
