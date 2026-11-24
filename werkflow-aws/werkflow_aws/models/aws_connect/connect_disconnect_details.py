from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisconnectDetails(BaseModel):
    PotentialDisconnectIssue: StrictStr | None = None
