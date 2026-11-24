from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeEventSubscriptionsRequest(BaseModel):
    SubscriptionName: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
    TagValues: list[StrictStr] | None = None
