from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_email_address_config import ConnectEmailAddressConfig


class ConnectAssociateQueueEmailAddressesRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    EmailAddressesConfig: list[ConnectEmailAddressConfig]
    ClientToken: StrictStr | None = None
