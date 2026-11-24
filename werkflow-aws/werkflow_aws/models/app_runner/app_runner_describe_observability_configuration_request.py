from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDescribeObservabilityConfigurationRequest(BaseModel):
    ObservabilityConfigurationArn: StrictStr
