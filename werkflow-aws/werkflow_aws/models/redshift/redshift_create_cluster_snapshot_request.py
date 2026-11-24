from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateClusterSnapshotRequest(BaseModel):
    SnapshotIdentifier: StrictStr
    ClusterIdentifier: StrictStr
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    Tags: list[RedshiftTag] | None = None
