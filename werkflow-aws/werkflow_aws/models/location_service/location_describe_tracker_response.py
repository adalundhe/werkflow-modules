from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class LocationDescribeTrackerResponse(BaseModel):
    TrackerName: StrictStr | None = None
    TrackerArn: StrictStr | None = None
    Description: StrictStr | None = None
    PricingPlan: StrictStr | None = None
    PricingPlanDataSource: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    PositionFiltering: StrictStr | None = None
    EventBridgeEnabled: StrictBool | None = None
    KmsKeyEnableGeospatialQueries: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
