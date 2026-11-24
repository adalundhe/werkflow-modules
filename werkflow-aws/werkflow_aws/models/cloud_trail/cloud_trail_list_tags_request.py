from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailListTagsRequest(BaseModel):
    ResourceIdList: list[StrictStr]
    NextToken: StrictStr | None = None
