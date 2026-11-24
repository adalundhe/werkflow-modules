from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontDeleteKeyGroupRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr | None = None
