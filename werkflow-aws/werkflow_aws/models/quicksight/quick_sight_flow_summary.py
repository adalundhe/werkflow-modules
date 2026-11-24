from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightFlowSummary(BaseModel):
    Arn: StrictStr | None = None
    FlowId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
    PublishState: StrictStr | None = None
    RunCount: StrictInt | None = None
    UserCount: StrictInt | None = None
    LastPublishedBy: StrictStr | None = None
    LastPublishedAt: datetime.datetime | StrictStr | None = None
