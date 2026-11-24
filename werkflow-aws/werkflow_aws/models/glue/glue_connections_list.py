from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueConnectionsList(BaseModel):
    Connections: list[StrictStr] | None = None
