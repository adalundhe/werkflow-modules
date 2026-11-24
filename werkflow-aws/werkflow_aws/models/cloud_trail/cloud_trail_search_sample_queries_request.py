from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudTrailSearchSampleQueriesRequest(BaseModel):
    SearchPhrase: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
