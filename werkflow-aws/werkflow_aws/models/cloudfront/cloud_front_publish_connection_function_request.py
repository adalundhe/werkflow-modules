from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontPublishConnectionFunctionRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
