from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConfigServiceOrganizationAggregationSource(BaseModel):
    RoleArn: StrictStr | None = None
    AwsRegions: list[StrictStr] | None = None
    AllAwsRegions: StrictBool | None = None
