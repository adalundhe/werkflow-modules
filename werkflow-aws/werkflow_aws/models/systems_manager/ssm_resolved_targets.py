from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SSMResolvedTargets(BaseModel):
    ParameterValues: list[StrictStr] | None = None
    Truncated: StrictBool | None = None
