from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_cluster_configuration import MemoryDBClusterConfiguration


class MemoryDBSnapshot(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Source: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ARN: StrictStr | None = None
    ClusterConfiguration: MemoryDBClusterConfiguration | None = None
    DataTiering: StrictStr | None = None
