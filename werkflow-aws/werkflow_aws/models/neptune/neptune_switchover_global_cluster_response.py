from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_global_cluster import NeptuneGlobalCluster


class NeptuneSwitchoverGlobalClusterResponse(BaseModel):
    GlobalCluster: NeptuneGlobalCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
