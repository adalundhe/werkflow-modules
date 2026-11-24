from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceAccountAggregationSource(BaseModel):
    AccountIds: list[StrictStr] | None = None
    AllAwsRegions: StrictBool | None = None
    AwsRegions: list[StrictStr] | None = None
