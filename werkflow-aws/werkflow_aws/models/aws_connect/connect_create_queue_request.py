from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_email_address_config import ConnectEmailAddressConfig
from .connect_outbound_caller_config import ConnectOutboundCallerConfig
from .connect_outbound_email_config import ConnectOutboundEmailConfig


class ConnectCreateQueueRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    HoursOfOperationId: StrictStr
    Description: StrictStr | None = None
    OutboundCallerConfig: ConnectOutboundCallerConfig | None = None
    OutboundEmailConfig: ConnectOutboundEmailConfig | None = None
    MaxContacts: StrictInt | None = None
    QuickConnectIds: list[StrictStr] | None = None
    EmailAddressesConfig: list[ConnectEmailAddressConfig] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
