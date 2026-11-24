from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendEntityTypesListItem(BaseModel):
    Type: StrictStr | None = None
