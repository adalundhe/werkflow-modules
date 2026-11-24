from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EMRInstanceGroupDetail(BaseModel):
    InstanceGroupId: StrictStr | None = None
    Name: StrictStr | None = None
    Market: StrictStr | None = None
    InstanceRole: StrictStr | None = None
    BidPrice: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceRequestCount: StrictInt | None = None
    InstanceRunningCount: StrictInt | None = None
    State: StrictStr | None = None
    LastStateChangeReason: StrictStr | None = None
    CreationDateTime: datetime.datetime | StrictStr | None = None
    StartDateTime: datetime.datetime | StrictStr | None = None
    ReadyDateTime: datetime.datetime | StrictStr | None = None
    EndDateTime: datetime.datetime | StrictStr | None = None
    CustomAmiId: StrictStr | None = None
