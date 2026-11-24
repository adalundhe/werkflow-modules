from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxAutoImportPolicy(BaseModel):
    Events: list[StrictStr] | None = None
