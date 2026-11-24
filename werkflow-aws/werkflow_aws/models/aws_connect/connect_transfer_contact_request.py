from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTransferContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ContactFlowId: StrictStr
    QueueId: StrictStr | None = None
    UserId: StrictStr | None = None
    ClientToken: StrictStr | None = None
