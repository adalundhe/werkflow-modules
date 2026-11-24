from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster_version import RedshiftClusterVersion


class RedshiftDescribeClusterVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    ClusterVersions: list[RedshiftClusterVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
