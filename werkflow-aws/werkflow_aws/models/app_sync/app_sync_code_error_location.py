from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppSyncCodeErrorLocation(BaseModel):
    line: StrictInt | None = None
    column: StrictInt | None = None
    span: StrictInt | None = None
