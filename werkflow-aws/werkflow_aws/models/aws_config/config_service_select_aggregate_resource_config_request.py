from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceSelectAggregateResourceConfigRequest(BaseModel):
    Expression: StrictStr
    ConfigurationAggregatorName: StrictStr
    Limit: StrictInt | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
