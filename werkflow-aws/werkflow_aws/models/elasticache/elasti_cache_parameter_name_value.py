from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheParameterNameValue(BaseModel):
    ParameterName: StrictStr | None = None
    ParameterValue: StrictStr | None = None
