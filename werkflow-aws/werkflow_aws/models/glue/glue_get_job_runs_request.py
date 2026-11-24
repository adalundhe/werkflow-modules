from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetJobRunsRequest(BaseModel):
    JobName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
