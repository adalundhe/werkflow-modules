from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxAutoExportPolicy(BaseModel):
    Events: list[StrictStr] | None = None
