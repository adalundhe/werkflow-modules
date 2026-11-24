from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .scope import Scope


class Context(BaseModel):
    id: StrictInt | None = None
    name: StrictStr | None = None
    scope: Scope | None = None
