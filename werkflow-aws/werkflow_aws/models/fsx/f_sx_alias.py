from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxAlias(BaseModel):
    Name: StrictStr | None = None
    Lifecycle: StrictStr | None = None
