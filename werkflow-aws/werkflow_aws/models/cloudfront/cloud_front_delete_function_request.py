from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteFunctionRequest(BaseModel):
    Name: StrictStr
    IfMatch: StrictStr
