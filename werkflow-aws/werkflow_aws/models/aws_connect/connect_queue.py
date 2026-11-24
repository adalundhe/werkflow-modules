from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_outbound_caller_config import ConnectOutboundCallerConfig
from .connect_outbound_email_config import ConnectOutboundEmailConfig


class ConnectQueue(BaseModel):
    Name: StrictStr | None = None
    QueueArn: StrictStr | None = None
    QueueId: StrictStr | None = None
    Description: StrictStr | None = None
    OutboundCallerConfig: ConnectOutboundCallerConfig | None = None
    OutboundEmailConfig: ConnectOutboundEmailConfig | None = None
    HoursOfOperationId: StrictStr | None = None
    MaxContacts: StrictInt | None = None
    Status: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
