from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueGetWorkflowRunsRequest(BaseModel):
    Name: StrictStr
    IncludeGraph: StrictBool | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
