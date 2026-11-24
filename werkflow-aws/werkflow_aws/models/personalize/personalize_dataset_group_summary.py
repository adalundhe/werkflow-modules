from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeDatasetGroupSummary(BaseModel):
    name: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
    domain: StrictStr | None = None
