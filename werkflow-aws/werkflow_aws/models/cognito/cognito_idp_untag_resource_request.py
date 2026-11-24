from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
