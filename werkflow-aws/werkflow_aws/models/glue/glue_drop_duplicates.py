from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDropDuplicates(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Columns: list[list[StrictStr]] | None = None
