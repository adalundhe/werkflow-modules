from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregatorFilterServicePrincipal(BaseModel):
    Type: StrictStr | None = None
    Value: list[StrictStr] | None = None
