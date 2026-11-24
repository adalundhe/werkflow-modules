from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamQueryListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
