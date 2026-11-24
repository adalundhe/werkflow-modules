from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseDatabaseTableList(BaseModel):
    Include: list[StrictStr] | None = None
    Exclude: list[StrictStr] | None = None
