from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2HttpHeaderConditionConfig(BaseModel):
    HttpHeaderName: StrictStr | None = None
    Values: list[StrictStr] | None = None
    RegexValues: list[StrictStr] | None = None
