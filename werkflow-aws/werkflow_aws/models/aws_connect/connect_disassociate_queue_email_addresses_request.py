from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateQueueEmailAddressesRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    EmailAddressesId: list[StrictStr]
    ClientToken: StrictStr | None = None
