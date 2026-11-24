from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUnion(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    UnionType: StrictStr | None = None
