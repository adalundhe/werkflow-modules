from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class EventBridgeDeleteConnectionResponse(BaseModel):
    ConnectionArn: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastAuthorizedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
