from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListTriggersRequest(BaseModel):
    NextToken: StrictStr | None = None
    DependentJobName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
