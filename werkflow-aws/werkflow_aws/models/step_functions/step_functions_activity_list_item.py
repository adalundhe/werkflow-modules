from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class StepFunctionsActivityListItem(BaseModel):
    activityArn: StrictStr | None = None
    name: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
