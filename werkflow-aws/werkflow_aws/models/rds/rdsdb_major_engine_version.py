from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_supported_engine_lifecycle import RDSSupportedEngineLifecycle


class RDSDBMajorEngineVersion(BaseModel):
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
    SupportedEngineLifecycles: list[RDSSupportedEngineLifecycle] | None = None
