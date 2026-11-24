from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeDatasetSummary(BaseModel):
    name: StrictStr | None = None
    datasetArn: StrictStr | None = None
    datasetType: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
