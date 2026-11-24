from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeSolutionSummary(BaseModel):
    name: StrictStr | None = None
    solutionArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    recipeArn: StrictStr | None = None
