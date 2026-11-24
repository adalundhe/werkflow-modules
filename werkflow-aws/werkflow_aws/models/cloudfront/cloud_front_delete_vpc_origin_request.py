from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteVpcOriginRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
