from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourceArnList: list[StrictStr] | None = None
