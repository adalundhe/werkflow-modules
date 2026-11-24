from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MoveFieldBean(BaseModel):
    after: StrictStr | None = None
    position: StrictStr | None = None
