from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueMerge(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Source: StrictStr | None = None
    PrimaryKeys: list[list[StrictStr]] | None = None
