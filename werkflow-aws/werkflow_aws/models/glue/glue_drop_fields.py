from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDropFields(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Paths: list[list[StrictStr]] | None = None
