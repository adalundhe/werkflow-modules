from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FieldIdIdentifier(BaseModel):
    identifier: StrictStr | None = None
    type: StrictStr | None = None
