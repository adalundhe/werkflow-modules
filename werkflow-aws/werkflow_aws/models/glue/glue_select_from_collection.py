from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueSelectFromCollection(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Index: StrictInt | None = None
