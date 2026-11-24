from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EventBridgeUpdateArchiveRequest(BaseModel):
    ArchiveName: StrictStr
    Description: StrictStr | None = None
    EventPattern: StrictStr | None = None
    RetentionDays: StrictInt | None = None
    KmsKeyIdentifier: StrictStr | None = None
