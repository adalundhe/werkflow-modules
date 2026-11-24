from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInstanceGroupHealthCheckConfiguration(BaseModel):
    InstanceGroupName: StrictStr | None = None
    InstanceIds: list[StrictStr] | None = None
    DeepHealthChecks: list[StrictStr] | None = None
