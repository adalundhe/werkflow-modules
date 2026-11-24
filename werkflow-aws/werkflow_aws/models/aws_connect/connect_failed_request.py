from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectFailedRequest(BaseModel):
    RequestIdentifier: StrictStr | None = None
    FailureReasonCode: StrictStr | None = None
    FailureReasonMessage: StrictStr | None = None
