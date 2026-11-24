from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferUntagResourceRequest(BaseModel):
    Arn: StrictStr
    TagKeys: list[StrictStr]
