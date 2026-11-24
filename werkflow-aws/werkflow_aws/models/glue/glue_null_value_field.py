from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_datatype import GlueDatatype


class GlueNullValueField(BaseModel):
    Value: StrictStr | None = None
    Datatype: GlueDatatype | None = None
