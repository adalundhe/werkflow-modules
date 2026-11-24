from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_replication_destination import ECRReplicationDestination


class ECRStartReplicationBackfillRequest(BaseModel):
    destination: ECRReplicationDestination
    registryId: StrictStr | None = None
