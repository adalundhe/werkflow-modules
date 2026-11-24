from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ScreenTypes(BaseModel):
    create: StrictInt | None = None
    default: StrictInt | None = None
    edit: StrictInt | None = None
    view: StrictInt | None = None
