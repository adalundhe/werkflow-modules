from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppRunnerObservabilityConfigurationSummary(BaseModel):
    ObservabilityConfigurationArn: StrictStr | None = None
    ObservabilityConfigurationName: StrictStr | None = None
    ObservabilityConfigurationRevision: StrictInt | None = None
