from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseDatabaseColumnList(BaseModel):
    Include: list[StrictStr] | None = None
    Exclude: list[StrictStr] | None = None
