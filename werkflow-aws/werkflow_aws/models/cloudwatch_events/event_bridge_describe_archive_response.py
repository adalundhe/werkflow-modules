from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeDescribeArchiveResponse(BaseModel):
    ArchiveArn: StrictStr | None = None
    ArchiveName: StrictStr | None = None
    EventSourceArn: StrictStr | None = None
    Description: StrictStr | None = None
    EventPattern: StrictStr | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
    KmsKeyIdentifier: StrictStr | None = None
    RetentionDays: StrictInt | None = None
    SizeBytes: StrictInt | None = None
    EventCount: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
