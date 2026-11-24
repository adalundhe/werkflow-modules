from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_engine_defaults import NeptuneEngineDefaults


class NeptuneDescribeEngineDefaultParametersResponse(BaseModel):
    EngineDefaults: NeptuneEngineDefaults | None = None
    ResponseMetadata: dict[str, Any] | None = None
