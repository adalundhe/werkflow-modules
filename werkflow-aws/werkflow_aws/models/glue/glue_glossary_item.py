from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGlossaryItem(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
