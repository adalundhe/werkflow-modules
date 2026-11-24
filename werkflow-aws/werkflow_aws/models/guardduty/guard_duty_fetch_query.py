from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_fetch_criterion import GuardDutyFetchCriterion
from .guard_duty_fetch_time_window import GuardDutyFetchTimeWindow


class GuardDutyFetchQuery(BaseModel):
    Criteria: list[GuardDutyFetchCriterion] | None = None
    TimeWindow: GuardDutyFetchTimeWindow | None = None
    RowLimit: StrictInt | None = None
    AccountId: StrictStr | None = None
    Indicator: StrictStr | None = None
    IndicatorType: StrictStr | None = None
    FindingType: StrictStr | None = None
    FindingId: StrictStr | None = None
