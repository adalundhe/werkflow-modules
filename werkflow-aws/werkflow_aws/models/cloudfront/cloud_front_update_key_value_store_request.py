from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontUpdateKeyValueStoreRequest(BaseModel):
    Name: StrictStr
    Comment: StrictStr
    IfMatch: StrictStr
