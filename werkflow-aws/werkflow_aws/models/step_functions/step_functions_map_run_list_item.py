from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class StepFunctionsMapRunListItem(BaseModel):
    executionArn: StrictStr | None = None
    mapRunArn: StrictStr | None = None
    stateMachineArn: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    stopDate: datetime.datetime | StrictStr | None = None
