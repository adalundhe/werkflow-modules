from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SageMakerProfilerConfig(BaseModel):
    S3OutputPath: StrictStr | None = None
    ProfilingIntervalInMilliseconds: StrictInt | None = None
    ProfilingParameters: dict[StrictStr, StrictStr] | None = None
    DisableProfiler: StrictBool | None = None
