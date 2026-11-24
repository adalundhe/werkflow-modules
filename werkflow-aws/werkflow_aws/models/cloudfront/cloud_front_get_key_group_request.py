from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetKeyGroupRequest(BaseModel):
    Id: StrictStr
