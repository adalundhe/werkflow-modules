from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFormationStackResourceDriftInformation(BaseModel):
    StackResourceDriftStatus: StrictStr | None = None
    LastCheckTimestamp: datetime.datetime | StrictStr | None = None
