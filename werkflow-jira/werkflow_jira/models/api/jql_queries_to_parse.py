from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JqlQueriesToParse(BaseModel):
    queries: list[StrictStr] | None = None
