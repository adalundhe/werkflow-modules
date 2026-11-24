from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .scope import Scope


class Screen(BaseModel):
    description: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    scope: Scope | None = None
