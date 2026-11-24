from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_replication_status_summary import ConnectReplicationStatusSummary


class ConnectReplicationConfiguration(BaseModel):
    ReplicationStatusSummaryList: list[ConnectReplicationStatusSummary] | None = None
    SourceRegion: StrictStr | None = None
    GlobalSignInEndpoint: StrictStr | None = None
