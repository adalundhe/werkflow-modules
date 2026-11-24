from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class RDSBacktrackDBClusterResponse(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    BacktrackIdentifier: StrictStr | None = None
    BacktrackTo: datetime.datetime | StrictStr | None = None
    BacktrackedFrom: datetime.datetime | StrictStr | None = None
    BacktrackRequestCreationTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
