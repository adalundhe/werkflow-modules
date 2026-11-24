from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueJoinColumn(BaseModel):
    From: StrictStr | None = None
    Keys: list[list[StrictStr]] | None = None
