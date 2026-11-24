from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDatatype(BaseModel):
    Id: StrictStr | None = None
    Label: StrictStr | None = None
