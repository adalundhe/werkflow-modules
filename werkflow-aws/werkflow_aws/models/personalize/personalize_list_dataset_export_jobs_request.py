from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListDatasetExportJobsRequest(BaseModel):
    datasetArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
