from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaFilterDefinition(BaseModel):
    Name: StrictStr | None = None
