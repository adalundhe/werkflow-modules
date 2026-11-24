from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2VersionToPublish(BaseModel):
    AssociatedRuleGroupArn: StrictStr | None = None
    ForecastedLifetime: StrictInt | None = None
