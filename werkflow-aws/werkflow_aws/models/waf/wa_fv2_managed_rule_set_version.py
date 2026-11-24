from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class WAFv2ManagedRuleSetVersion(BaseModel):
    AssociatedRuleGroupArn: StrictStr | None = None
    Capacity: StrictInt | None = None
    ForecastedLifetime: StrictInt | None = None
    PublishTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    ExpiryTimestamp: datetime.datetime | StrictStr | None = None
