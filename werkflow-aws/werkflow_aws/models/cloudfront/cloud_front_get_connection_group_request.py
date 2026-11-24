from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGetConnectionGroupRequest(BaseModel):
    Identifier: StrictStr
