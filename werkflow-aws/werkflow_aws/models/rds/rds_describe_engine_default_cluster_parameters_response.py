from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_engine_defaults import RDSEngineDefaults


class RDSDescribeEngineDefaultClusterParametersResponse(BaseModel):
    EngineDefaults: RDSEngineDefaults | None = None
    ResponseMetadata: dict[str, Any] | None = None
