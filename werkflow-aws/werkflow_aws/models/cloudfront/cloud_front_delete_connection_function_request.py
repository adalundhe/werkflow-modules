from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteConnectionFunctionRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
