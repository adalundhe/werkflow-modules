from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IotAnalyticsAction(BaseModel):
    channelArn: StrictStr | None = None
    channelName: StrictStr | None = None
    batchMode: StrictBool | None = None
    roleArn: StrictStr | None = None
