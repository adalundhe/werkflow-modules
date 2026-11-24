from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaListCalculationExecutionsRequest(BaseModel):
    SessionId: StrictStr
    StateFilter: Literal['CREATING', 'CREATED', 'QUEUED', 'RUNNING', 'CANCELING', 'CANCELED', 'COMPLETED', 'FAILED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
