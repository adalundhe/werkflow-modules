from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSqlAlias(BaseModel):
    From: StrictStr | None = None
    Alias: StrictStr | None = None
