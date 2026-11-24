from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontPublishFunctionRequest(BaseModel):
    Name: StrictStr
    IfMatch: StrictStr
