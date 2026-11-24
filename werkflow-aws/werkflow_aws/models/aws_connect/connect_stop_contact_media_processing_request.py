from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectStopContactMediaProcessingRequest(BaseModel):
    InstanceId: StrictStr | None = None
    ContactId: StrictStr | None = None
