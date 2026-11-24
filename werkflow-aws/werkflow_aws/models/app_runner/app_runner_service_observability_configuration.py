from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppRunnerServiceObservabilityConfiguration(BaseModel):
    ObservabilityEnabled: StrictBool | None = None
    ObservabilityConfigurationArn: StrictStr | None = None
