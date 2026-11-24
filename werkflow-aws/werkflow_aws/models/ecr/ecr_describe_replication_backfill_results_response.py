from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_replication_backfill_progress import ECRReplicationBackfillProgress
from .ecr_replication_backfill_result import ECRReplicationBackfillResult
from .ecr_replication_destination import ECRReplicationDestination


class ECRDescribeReplicationBackfillResultsResponse(BaseModel):
    registryId: StrictStr | None = None
    replicationBackfillId: StrictStr | None = None
    destination: ECRReplicationDestination | None = None
    status: StrictStr | None = None
    failureCode: StrictStr | None = None
    progress: ECRReplicationBackfillProgress | None = None
    results: list[ECRReplicationBackfillResult] | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    endedAt: datetime.datetime | StrictStr | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
