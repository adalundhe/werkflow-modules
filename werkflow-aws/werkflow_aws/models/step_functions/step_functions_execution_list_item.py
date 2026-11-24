from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsExecutionListItem(BaseModel):
    executionArn: StrictStr | None = None
    stateMachineArn: StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    startDate: datetime.datetime | StrictStr | None = None
    stopDate: datetime.datetime | StrictStr | None = None
    mapRunArn: StrictStr | None = None
    itemCount: StrictInt | None = None
    stateMachineVersionArn: StrictStr | None = None
    stateMachineAliasArn: StrictStr | None = None
    redriveCount: StrictInt | None = None
    redriveDate: datetime.datetime | StrictStr | None = None
