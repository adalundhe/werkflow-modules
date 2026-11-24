from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceSelectResourceConfigRequest(BaseModel):
    Expression: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
