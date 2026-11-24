from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailChannel(BaseModel):
    ChannelArn: StrictStr | None = None
    Name: StrictStr | None = None
