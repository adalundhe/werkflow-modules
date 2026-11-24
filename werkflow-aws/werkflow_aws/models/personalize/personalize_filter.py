from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeFilter(BaseModel):
    name: StrictStr | None = None
    filterArn: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    failureReason: StrictStr | None = None
    filterExpression: StrictStr | None = None
    status: StrictStr | None = None
