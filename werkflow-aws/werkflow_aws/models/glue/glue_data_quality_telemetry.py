from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueDataQualityTelemetry(BaseModel):
    VcpuHours: StrictFloat | StrictInt | None = None
    FlagsEnabled: dict[StrictStr, StrictStr] | None = None
    LibraryVersion: StrictStr | None = None
    SparkVersion: StrictStr | None = None
    HostRuntimeVersion: StrictStr | None = None
    Engine: Literal['SPARK', 'PYTHON'] | None = None
