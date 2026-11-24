from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53UpdateHostedZoneCommentRequest(BaseModel):
    Id: StrictStr
    Comment: StrictStr | None = None
