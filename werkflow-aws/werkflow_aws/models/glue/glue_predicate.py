from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_condition import GlueCondition


class GluePredicate(BaseModel):
    Logical: StrictStr | None = None
    Conditions: list[GlueCondition] | None = None
