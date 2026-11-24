from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
