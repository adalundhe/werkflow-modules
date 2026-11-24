from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceAggregatorFilterResourceType(BaseModel):
    Type: StrictStr | None = None
    Value: list[StrictStr] | None = None
