from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRDescribeJobFlowsRequest(BaseModel):
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    JobFlowIds: list[StrictStr] | None = None
    JobFlowStates: list[Literal['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'SHUTTING_DOWN', 'TERMINATED', 'COMPLETED', 'FAILED']] | None = None
