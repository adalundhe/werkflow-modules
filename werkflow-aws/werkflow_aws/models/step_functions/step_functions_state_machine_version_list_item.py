from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class StepFunctionsStateMachineVersionListItem(BaseModel):
    stateMachineVersionArn: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
