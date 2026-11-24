from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetBlueprintRunsRequest(BaseModel):
    BlueprintName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
