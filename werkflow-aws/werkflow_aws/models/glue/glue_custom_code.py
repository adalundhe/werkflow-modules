from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueCustomCode(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Code: StrictStr | None = None
    ClassName: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
