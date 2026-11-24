from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKReplicationInfoSummary(BaseModel):
    SourceKafkaClusterAlias: StrictStr | None = None
    TargetKafkaClusterAlias: StrictStr | None = None
