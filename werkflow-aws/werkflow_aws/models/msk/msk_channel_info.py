from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MSKChannelInfo(BaseModel):
    ChannelArn: StrictStr | None = None
    ChannelName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DestinationType: StrictStr | None = None
    ClusterOperationArn: StrictStr | None = None
