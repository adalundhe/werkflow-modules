from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_api_call import GuardDutyApiCall


class GuardDutyActivity(BaseModel):
    Type: StrictStr | None = None
    Api: GuardDutyApiCall | None = None
