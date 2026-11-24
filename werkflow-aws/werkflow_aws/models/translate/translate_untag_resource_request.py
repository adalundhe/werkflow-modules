from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
