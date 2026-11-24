from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .pinpoint_base_kpi_result import PinpointBaseKpiResult


class PinpointJourneyDateRangeKpiResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    JourneyId: StrictStr | None = None
    KpiName: StrictStr | None = None
    KpiResult: PinpointBaseKpiResult | None = None
    NextToken: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
