from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_cluster_summary import EMRClusterSummary


class EMRListClustersResponse(BaseModel):
    Clusters: list[EMRClusterSummary] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
