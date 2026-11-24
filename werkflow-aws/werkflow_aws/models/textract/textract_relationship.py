from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractRelationship(BaseModel):
    Type: StrictStr | None = None
    Ids: list[StrictStr] | None = None
