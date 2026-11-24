from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_fetch_query import GuardDutyFetchQuery
from .guard_duty_fetch_result import GuardDutyFetchResult


class GuardDutyFetchRecord(BaseModel):
    FetchType: StrictStr | None = None
    Query: GuardDutyFetchQuery | None = None
    Result: GuardDutyFetchResult | None = None
