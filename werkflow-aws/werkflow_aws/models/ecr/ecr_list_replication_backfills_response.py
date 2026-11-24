from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_replication_backfill_summary import ECRReplicationBackfillSummary


class ECRListReplicationBackfillsResponse(BaseModel):
    registryId: StrictStr | None = None
    backfills: list[ECRReplicationBackfillSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
