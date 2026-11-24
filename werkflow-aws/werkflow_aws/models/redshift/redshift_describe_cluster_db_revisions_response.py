from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster_db_revision import RedshiftClusterDbRevision


class RedshiftDescribeClusterDbRevisionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ClusterDbRevisions: list[RedshiftClusterDbRevision] | None = None
    ResponseMetadata: dict[str, Any] | None = None
