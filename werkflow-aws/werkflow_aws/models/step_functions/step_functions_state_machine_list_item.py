from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class StepFunctionsStateMachineListItem(BaseModel):
    stateMachineArn: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
