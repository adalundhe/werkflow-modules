from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ScreenableTab(BaseModel):
    id: StrictInt | None = None
    name: StrictStr | None = None
