from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListDataDeletionJobsRequest(BaseModel):
    datasetGroupArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
