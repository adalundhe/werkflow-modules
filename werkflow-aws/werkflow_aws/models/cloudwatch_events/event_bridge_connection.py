from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EventBridgeConnection(BaseModel):
    ConnectionArn: StrictStr | None = None
    Name: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    StateReason: StrictStr | None = None
    AuthorizationType: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastAuthorizedTime: datetime.datetime | StrictStr | None = None
