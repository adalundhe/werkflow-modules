from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendRelationshipsListItem(BaseModel):
    Ids: list[StrictStr] | None = None
    Type: StrictStr | None = None
