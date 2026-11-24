from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PinpointGetCampaignDateRangeKpiRequest(BaseModel):
    ApplicationId: StrictStr
    CampaignId: StrictStr
    KpiName: StrictStr
    EndTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
