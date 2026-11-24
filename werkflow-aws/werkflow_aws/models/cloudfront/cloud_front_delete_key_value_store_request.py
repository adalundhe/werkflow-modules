from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteKeyValueStoreRequest(BaseModel):
    Name: StrictStr
    IfMatch: StrictStr
