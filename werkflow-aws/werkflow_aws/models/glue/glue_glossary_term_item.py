from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGlossaryTermItem(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ShortDescription: StrictStr | None = None
