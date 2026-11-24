from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeSolutionVersionSummary(BaseModel):
    solutionVersionArn: StrictStr | None = None
    status: StrictStr | None = None
    trainingMode: StrictStr | None = None
    trainingType: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
