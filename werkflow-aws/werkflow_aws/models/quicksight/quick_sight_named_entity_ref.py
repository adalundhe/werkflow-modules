from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightNamedEntityRef(BaseModel):
    NamedEntityName: StrictStr | None = None
