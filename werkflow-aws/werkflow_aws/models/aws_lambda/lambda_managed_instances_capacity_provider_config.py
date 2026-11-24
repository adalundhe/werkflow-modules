from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LambdaManagedInstancesCapacityProviderConfig(BaseModel):
    CapacityProviderArn: StrictStr
    PerExecutionEnvironmentMaxConcurrency: StrictInt | None = None
    ExecutionEnvironmentMemoryGiBPerVCpu: StrictFloat | StrictInt | None = None
