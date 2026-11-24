from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class MSKBrokerCountUpdateInfo(BaseModel):
    CreatedBrokerIds: list[StrictFloat | StrictInt] | None = None
    DeletedBrokerIds: list[StrictFloat | StrictInt] | None = None
