from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRListClustersRequest(BaseModel):
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    ClusterStates: list[Literal['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING', 'TERMINATING', 'TERMINATED', 'TERMINATED_WITH_ERRORS']] | None = None
    Marker: StrictStr | None = None
