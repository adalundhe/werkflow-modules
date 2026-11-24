from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointActivityResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    CampaignId: StrictStr | None = None
    End: StrictStr | None = None
    Id: StrictStr | None = None
    Result: StrictStr | None = None
    ScheduledStart: StrictStr | None = None
    Start: StrictStr | None = None
    State: StrictStr | None = None
    SuccessfulEndpointCount: StrictInt | None = None
    TimezonesCompletedCount: StrictInt | None = None
    TimezonesTotalCount: StrictInt | None = None
    TotalEndpointCount: StrictInt | None = None
    TreatmentId: StrictStr | None = None
    ExecutionMetrics: dict[StrictStr, StrictStr] | None = None
