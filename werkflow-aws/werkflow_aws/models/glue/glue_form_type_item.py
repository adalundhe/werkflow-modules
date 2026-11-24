from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFormTypeItem(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
