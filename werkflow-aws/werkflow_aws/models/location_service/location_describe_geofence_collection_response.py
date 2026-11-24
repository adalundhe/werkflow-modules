from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class LocationDescribeGeofenceCollectionResponse(BaseModel):
    CollectionName: StrictStr | None = None
    CollectionArn: StrictStr | None = None
    Description: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    PricingPlanDataSource: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    GeofenceCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
