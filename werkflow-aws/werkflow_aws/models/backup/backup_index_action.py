from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupIndexAction(BaseModel):
    ResourceTypes: list[StrictStr] | None = None
