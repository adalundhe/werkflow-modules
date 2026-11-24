from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectVirtualInterfaceTestHistory(BaseModel):
    testId: StrictStr | None = None
    virtualInterfaceId: StrictStr | None = None
    bgpPeers: list[StrictStr] | None = None
    status: StrictStr | None = None
    ownerAccount: StrictStr | None = None
    testDurationInMinutes: StrictInt | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
