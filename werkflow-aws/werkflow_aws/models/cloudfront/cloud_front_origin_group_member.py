from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontOriginGroupMember(BaseModel):
    OriginId: StrictStr | None = None
