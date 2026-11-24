from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_cluster import ECSCluster
from .ecs_failure import ECSFailure


class ECSDescribeClustersResponse(BaseModel):
    clusters: list[ECSCluster] | None = None
    failures: list[ECSFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
