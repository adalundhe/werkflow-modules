from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ecr_replication_backfill_progress import ECRReplicationBackfillProgress
from .ecr_replication_destination import ECRReplicationDestination


class ECRReplicationBackfillSummary(BaseModel):
    replicationBackfillId: StrictStr | None = None
    destination: ECRReplicationDestination | None = None
    status: StrictStr | None = None
    failureCode: StrictStr | None = None
    progress: ECRReplicationBackfillProgress | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
