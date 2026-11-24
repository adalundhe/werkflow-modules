from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListBatchSegmentJobsRequest(BaseModel):
    solutionVersionArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
