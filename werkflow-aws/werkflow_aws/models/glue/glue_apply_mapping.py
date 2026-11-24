from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_mapping import GlueMapping


class GlueApplyMapping(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Mapping: list[GlueMapping] | None = None
