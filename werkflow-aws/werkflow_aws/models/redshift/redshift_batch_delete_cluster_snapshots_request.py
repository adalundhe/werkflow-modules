from __future__ import annotations
from pydantic import BaseModel
from .redshift_delete_cluster_snapshot_message import RedshiftDeleteClusterSnapshotMessage


class RedshiftBatchDeleteClusterSnapshotsRequest(BaseModel):
    Identifiers: list[RedshiftDeleteClusterSnapshotMessage]
