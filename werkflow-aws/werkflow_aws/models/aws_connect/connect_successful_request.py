from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSuccessfulRequest(BaseModel):
    RequestIdentifier: StrictStr | None = None
    ContactId: StrictStr | None = None
