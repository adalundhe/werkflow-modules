from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_cluster import ECSCluster


class ECSDeleteClusterResponse(BaseModel):
    cluster: ECSCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
