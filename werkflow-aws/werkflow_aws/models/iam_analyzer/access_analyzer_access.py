from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerAccess(BaseModel):
    actions: list[StrictStr] | None = None
    resources: list[StrictStr] | None = None
