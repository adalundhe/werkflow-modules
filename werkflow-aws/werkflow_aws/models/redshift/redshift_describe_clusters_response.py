from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_cluster import RedshiftCluster


class RedshiftDescribeClustersResponse(BaseModel):
    Marker: StrictStr | None = None
    Clusters: list[RedshiftCluster] | None = None
    ResponseMetadata: dict[str, Any] | None = None
