from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceDescribeConfigurationAggregatorSourcesStatusRequest(BaseModel):
    ConfigurationAggregatorName: StrictStr
    UpdateStatus: list[Literal['FAILED', 'SUCCEEDED', 'OUTDATED']] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
