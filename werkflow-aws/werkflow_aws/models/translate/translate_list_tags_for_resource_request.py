from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
