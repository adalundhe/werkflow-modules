from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EMRListSessionsRequest(BaseModel):
    ClusterId: StrictStr
    SessionStates: list[Literal['SUBMITTED', 'STARTING', 'STARTED', 'IDLE', 'BUSY', 'TERMINATING', 'TERMINATED', 'FAILED']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
