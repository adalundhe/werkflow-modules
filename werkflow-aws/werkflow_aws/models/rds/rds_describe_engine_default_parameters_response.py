from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_engine_defaults import RDSEngineDefaults


class RDSDescribeEngineDefaultParametersResponse(BaseModel):
    EngineDefaults: RDSEngineDefaults | None = None
    ResponseMetadata: dict[str, Any] | None = None
