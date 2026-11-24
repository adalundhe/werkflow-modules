from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaListExecutorsRequest(BaseModel):
    SessionId: StrictStr
    ExecutorStateFilter: Literal['CREATING', 'CREATED', 'REGISTERED', 'TERMINATING', 'TERMINATED', 'FAILED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
