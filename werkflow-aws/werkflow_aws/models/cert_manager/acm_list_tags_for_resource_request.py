from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
