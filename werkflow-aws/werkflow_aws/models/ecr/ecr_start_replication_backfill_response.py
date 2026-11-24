from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_replication_destination import ECRReplicationDestination


class ECRStartReplicationBackfillResponse(BaseModel):
    replicationBackfillId: StrictStr | None = None
    registryId: StrictStr | None = None
    destination: ECRReplicationDestination | None = None
    status: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
