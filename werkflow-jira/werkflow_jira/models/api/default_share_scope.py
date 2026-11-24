from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DefaultShareScope(BaseModel):
    scope: StrictStr | None = None
