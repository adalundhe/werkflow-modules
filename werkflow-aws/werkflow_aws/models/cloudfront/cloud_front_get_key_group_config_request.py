from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetKeyGroupConfigRequest(BaseModel):
    Id: StrictStr
