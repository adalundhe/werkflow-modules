from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceDescribeConfigurationAggregatorsRequest(BaseModel):
    ConfigurationAggregatorNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
